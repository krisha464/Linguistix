import streamlit as st
import datetime
import random
from config import WOTD_LIST, QUOTES
from utils.storage import load_data

def initialize_session_state():
    if 'authenticated' not in st.session_state: st.session_state.authenticated = False
    if 'username' not in st.session_state: st.session_state.username = None

    stored_data = load_data(st.session_state.username)
    if 'history' not in st.session_state:
        st.session_state.history = stored_data.get("history", [])
        for item in st.session_state.history:
            if 'Time' not in item: item['Time'] = datetime.datetime.now().strftime("%H:%M:%S")
    if 'favorites' not in st.session_state: st.session_state.favorites = stored_data.get("favorites", [])
    if 'phrasebook' not in st.session_state: st.session_state.phrasebook = stored_data.get("phrasebook", [])
    if 'input_text' not in st.session_state: st.session_state.input_text = ""
    if 'src_lang' not in st.session_state: st.session_state.src_lang = "auto"
    if 'tgt_lang' not in st.session_state: st.session_state.tgt_lang = "es"
    if 'conv_history' not in st.session_state: st.session_state.conv_history = []
    if 'conv_lang_a' not in st.session_state: st.session_state.conv_lang_a = "en"
    if 'conv_lang_b' not in st.session_state: st.session_state.conv_lang_b = "es"
    if 'audio_to_play' not in st.session_state: st.session_state.audio_to_play = None
    if 'dict_word' not in st.session_state: st.session_state.dict_word = ""
    if 'dict_results' not in st.session_state: st.session_state.dict_results = None
    if 'translation_result' not in st.session_state: st.session_state.translation_result = None
    if 'visual_ocr_img' not in st.session_state: st.session_state.visual_ocr_img = None
    if 'ocr_result' not in st.session_state: st.session_state.ocr_result = None
    if 'ocr_detected' not in st.session_state: st.session_state.ocr_detected = None
    if 'ocr_raw' not in st.session_state: st.session_state.ocr_raw = None
    if 'doc_result' not in st.session_state: st.session_state.doc_result = None
    if 'doc_detected' not in st.session_state: st.session_state.doc_detected = None
    if 'doc_raw_text' not in st.session_state: st.session_state.doc_raw_text = None
    if 'page' not in st.session_state: st.session_state.page = "main"
    if 'show_dashboard' not in st.session_state: st.session_state.show_dashboard = False

    if 'dict_show_scenarios' not in st.session_state: st.session_state.dict_show_scenarios = False
    if 'active_game' not in st.session_state: st.session_state.active_game = None
    if 'wotd' not in st.session_state: st.session_state.wotd = random.choice(WOTD_LIST)
    if 'quote' not in st.session_state: st.session_state.quote = random.choice(QUOTES)

    # Word Game States
    if 'word_games_selected' not in st.session_state: st.session_state.word_games_selected = None
    if 'game_step' not in st.session_state: st.session_state.game_step = 1
    for g in ['quiz', 'syn', 'detect', 'context', 'speed']:
        if f'{g}_total' not in st.session_state: st.session_state[f'{g}_total'] = 0
        if f'{g}_score' not in st.session_state: st.session_state[f'{g}_score'] = 0
        if f'{g}_feedback' not in st.session_state: st.session_state[f'{g}_feedback'] = None

def swap_languages():
    if st.session_state.src_lang != "auto":
        s, t = st.session_state.src_lang, st.session_state.tgt_lang
        st.session_state.src_lang, st.session_state.tgt_lang = t, s

def get_base64_bin_file(bin_file):
    import base64
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
