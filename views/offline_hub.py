import streamlit as st
from utils.translator import SUPPORTED_LANGS
from utils.speech import text_to_speech
from utils.storage import save_data

def render_offline_hub():
    st.markdown("""
        <div style='text-align:center; margin-bottom:30px;'>
            <h3 style='margin:0; font-weight:800; color:var(--accent);'><i class='fas fa-plane-departure'></i> Global Offline Hub</h3>
            <p style='opacity:0.6; font-size:13px;'>Your travel companion, even without Wi-Fi</p>
        </div>
    """, unsafe_allow_html=True)
    
    # --- Quick Start Guide ---
    g_col1, g_col2, g_col3 = st.columns(3)
    guide_items = [
        {"icon": "🔖", "title": "1. SAVE", "text": "Bookmark phrases in the Translator.", "color": "var(--accent)"},
        {"icon": "📂", "title": "2. ACCESS", "text": "Find them here in your Phrasebook.", "color": "#f59e0b"},
        {"icon": "🔊", "title": "3. LISTEN", "text": "Play audio offline anytime.", "color": "#10b981"}
    ]
    for i, item in enumerate(guide_items):
        with [g_col1, g_col2, g_col3][i]:
            st.markdown(f"""
            <div style='background:var(--panel); border:1px solid var(--border); border-radius:20px; padding:20px; border-top:4px solid {item['color']}; min-height:120px;'>
                <p style='font-size:12px; font-weight:900; color:{item['color']}; margin-bottom:8px;'>{item['title']}</p>
                <p style='font-size:13px; margin:0; opacity:0.8;'>{item['text']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.markdown("<h4><i class='fas fa-book-bookmark'></i> Your Phrasebook Carousel</h4>", unsafe_allow_html=True)
    
    if not st.session_state.phrasebook:
        st.markdown("""
        <div style="text-align:center; padding: 60px 20px; background:var(--panel); border:2px dashed var(--border); border-radius:30px; margin-top:20px;">
            <div style="font-size:40px; margin-bottom:20px; opacity:0.3;">📭</div>
            <p style="font-size:18px; font-weight:700; color:var(--text-primary);">Your phrasebook is empty</p>
            <p style="font-size:13px; opacity:0.6; max-width:280px; margin: 0 auto;">Bookmark translations from the main tab to see them here.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Carousel CSS
        num_items = len(st.session_state.phrasebook)
        scroll_duration = max(20, num_items * 5) # Scale duration with items
        
        st.markdown(f"""
        <style>
            @keyframes scroll {{
                0% {{ transform: translateX(0); }}
                100% {{ transform: translateX(calc(-320px * {num_items})); }}
            }}
            .carousel-track {{
                display: flex;
                width: calc(320px * {num_items * 2});
                animation: scroll {scroll_duration}s linear infinite;
                padding: 20px 0;
            }}
            .carousel-track:hover {{
                animation-play-state: paused;
            }}
            .carousel-item {{
                width: 300px;
                margin-right: 20px;
                flex-shrink: 0;
                background: var(--panel);
                border: 1.5px solid var(--border);
                border-radius: 24px;
                padding: 24px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.05);
                transition: all 0.3s ease;
            }}
            .carousel-item:hover {{
                transform: translateY(-10px) scale(1.02);
                border-color: var(--accent);
                box-shadow: 0 20px 40px var(--glow);
            }}
        </style>
        """, unsafe_allow_html=True)

        # We double the list for seamless looping
        items_to_render = st.session_state.phrasebook + st.session_state.phrasebook if num_items > 2 else st.session_state.phrasebook

        st.markdown('<div style="overflow:hidden; padding:10px 0;">', unsafe_allow_html=True)
        st.markdown('<div class="carousel-track">', unsafe_allow_html=True)
        
        for idx, entry in enumerate(items_to_render):
            lang_name = SUPPORTED_LANGS.get(entry['lang'], entry['lang'])
            st.markdown(f"""
            <div class="carousel-item">
                <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;'>
                    <span style='background:var(--accent)15; color:var(--accent); padding:4px 10px; border-radius:8px; font-size:10px; font-weight:900;'>{lang_name.upper()}</span>
                    <span style='font-size:10px; opacity:0.4; font-weight:700;'>{entry.get("date", "Today")[:10]}</span>
                </div>
                <p style='font-size:13px; color:var(--text-secondary); margin-bottom:8px; font-style:italic;'>"{entry['input']}"</p>
                <p style='font-size:18px; color:var(--text-primary); font-weight:900; margin:0; line-height:1.3;'>{entry['output']}</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

        st.markdown("<p style='text-align:center; font-size:11px; opacity:0.5; margin-top:-10px;'>Hover to pause the carousel</p>", unsafe_allow_html=True)

        # Actions Section (Static controls for the actual list)
        st.markdown("<br><h4><i class='fas fa-list'></i> Manage Collection</h4>", unsafe_allow_html=True)
        for idx, entry in enumerate(reversed(st.session_state.phrasebook)):
            with st.container():
                c_text, c_play, c_del = st.columns([4, 1, 1])
                with c_text:
                    st.markdown(f"**{entry['output']}**  \n<small style='opacity:0.6;'>{entry['input']} ({SUPPORTED_LANGS.get(entry['lang'], entry['lang'])})</small>", unsafe_allow_html=True)
                with c_play:
                    if st.button(f"🔊", key=f"play_off_{idx}", use_container_width=True):
                        audio = text_to_speech(entry['output'], entry['lang'])
                        if audio:
                            st.session_state.audio_to_play = audio
                            st.rerun()
                with c_del:
                    if st.button(f"🗑️", key=f"rem_off_{idx}", use_container_width=True):
                        st.session_state.phrasebook.pop(-(idx+1))
                        save_data(st.session_state.history, st.session_state.favorites, st.session_state.phrasebook, username=st.session_state.username)
                        st.rerun()
                st.divider()
