import requests
import random

def get_random_game_question(game_type='quiz'):
    """
    Fetches a random English word and its dictionary info.
    Returns a formatted question dictionary for the game.
    """
    # High-quality fallback data to use if API fails or word info is sparse
    HARDCODED_CHALLENGES = [
        {"word": "Eloquent", "answer": "Fluent or persuasive in speaking or writing.", "example": "She gave an eloquent speech.", "synonym": "Fluent"},
        {"word": "Meticulous", "answer": "Showing great attention to detail; very careful and precise.", "example": "He was meticulous about his hair.", "synonym": "Precise"},
        {"word": "Pragmatic", "answer": "Dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations.", "example": "A pragmatic approach to politics.", "synonym": "Practical"},
        {"word": "Ephemeral", "answer": "Lasting for a very short time.", "example": "The ephemeral nature of fashion.", "synonym": "Short-lived"},
        {"word": "Loquacious", "answer": "Tending to talk a great deal; talkative.", "example": "A loquacious dinner guest.", "synonym": "Talkative"}
    ]
    
    try:
        # Try to get a real word from the API, but fall back gracefully
        word = random.choice([c['word'] for c in HARDCODED_CHALLENGES])
        try:
            r = requests.get("https://story-shack-cdn-v2.glitch.me/generators/word-generator?count=1", timeout=2)
            if r.status_code == 200:
                word = r.json()['data'][0]['word']
        except:
            pass # Use hardcoded word
            
        info = get_word_info(word)
        
        # If API word is valid and has meanings, extract data correctly
        if info and info.get('meanings') and len(info['meanings']) > 0:
            m = info['meanings'][0]
            if m.get('definitions') and len(m['definitions']) > 0:
                defn = m['definitions'][0].get('definition')
                ex = m['definitions'][0].get('example', "No example available.")
                
                # Try simple synonym extraction if it's the game type
                ans = defn if game_type == 'quiz' else "Equivalent"
                
                question = {
                    "word": info['word'].capitalize(),
                    "answer": ans,
                    "example": ex,
                    "type": "Definition" if game_type == 'quiz' else "Synonym"
                }

                # Generate distractors
                distractors = [
                    "Full of strong energy and enthusiasm.",
                    "Moving with great speed and momentum.",
                    "Uncertain or having multiple meanings.",
                    "Easily broken or damaged.",
                    "Done with great attention to detail.",
                    "Based on practical rather than theoretical ideas."
                ]
                import random as py_random
                choices = py_random.sample([d for d in distractors if d != question['answer']], 3)
                choices.append(question['answer'])
                py_random.shuffle(choices)
                question["choices"] = choices
                return question

        # If anything fails during extraction (API return 404 or missing keys), use a fallback challenge
        fallback = random.choice(HARDCODED_CHALLENGES)
        ans = fallback['answer'] if game_type == 'quiz' else fallback['synonym']
        
        distractors = ["Opposite", "Irrelevant", "Misleading", "Confusing", "Abstract", "Tangible"]
        import random as py_random
        choices = py_random.sample([d for d in distractors if d != ans], 3)
        choices.append(ans)
        py_random.shuffle(choices)
        
        return {
            "word": fallback['word'],
            "answer": ans,
            "example": fallback['example'],
            "type": "Definition" if game_type == 'quiz' else "Synonym",
            "choices": choices
        }
            
    except Exception as e:
        print(f"Random Question Error: {e}")
        return None

import random

def get_word_info(word):
    """
    Fetches word information from Free Dictionary API.
    Ensures all data (meanings, synonyms, antonyms) is synchronized for the same word.
    """
    if not word.strip():
        return None
    
    try:
        # 1. Fetch primary data from Dictionary API
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower().strip()}"
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            return None
            
        data = response.json()[0]
        actual_word = data.get("word", word).lower()
        
        result = {
            "word": actual_word.capitalize(),
            "phonetic": data.get("phonetic", ""),
            "meanings": [],
            "synonyms": [],
            "antonyms": []
        }
        
        # 2. Extract meanings and initial thesaurus data
        for meaning in data.get("meanings", []):
            part_of_speech = meaning.get("partOfSpeech")
            result["synonyms"].extend(meaning.get("synonyms", []))
            result["antonyms"].extend(meaning.get("antonyms", []))

            m_info = {"partOfSpeech": part_of_speech, "definitions": []}
            for definition in meaning.get("definitions", []):
                m_info["definitions"].append({
                    "definition": definition.get("definition"),
                    "example": definition.get("example")
                })
                result["synonyms"].extend(definition.get("synonyms", []))
                result["antonyms"].extend(definition.get("antonyms", []))
            result["meanings"].append(m_info)

        # 3. Synchronized Datamuse lookup using the 'actual_word' from the API
        try:
            # We fetch synonyms and antonyms specifically for the word the dictionary returned
            dm_syn_url = f"https://api.datamuse.com/words?rel_syn={actual_word}&max=15"
            dm_ant_url = f"https://api.datamuse.com/words?rel_ant={actual_word}&max=15"
            
            syn_res = requests.get(dm_syn_url, timeout=3)
            if syn_res.status_code == 200:
                result["synonyms"].extend([w['word'] for w in syn_res.json()])
                
            ant_res = requests.get(dm_ant_url, timeout=3)
            if ant_res.status_code == 200:
                result["antonyms"].extend([w['word'] for w in ant_res.json()])
        except:
            pass

        # 4. Final cleaning and de-duplication
        result["synonyms"] = sorted(list(set([s.lower() for s in result["synonyms"] if s.lower() != actual_word])), key=len)
        result["antonyms"] = sorted(list(set([a.lower() for a in result["antonyms"] if a.lower() != actual_word])), key=len)
        
        return result
    except Exception as e:
        print(f"Dictionary Sync Error: {e}")
        return None
