import streamlit as st
import random
import datetime
import time

# Config & Styles
from config import WOTD_LIST, QUOTES, THEMES
from views.ui_styles import get_main_css

# Utilities
from utils.session import initialize_session_state, swap_languages, get_base64_bin_file
from utils.translator import SUPPORTED_LANGS
from utils.pdf import create_pdf
from utils.storage import save_data

# Views
from views.auth import render_auth_page
from views.sidebar import render_sidebar
from views.translator import render_translator
from views.conversation import render_conversation
from views.dictionary_view import render_dictionary
from views.offline_hub import render_offline_hub
from views.image_translate import render_image_translate
from views.doc_translate import render_doc_translate
from views.fun_zone import render_fun_zone
from views.games import render_word_games
from views.dashboard import show_dashboard_modal

# Page Config
st.set_page_config(page_title="Linguistix", page_icon="✨", layout="centered", initial_sidebar_state="collapsed")

# Initialize Session State
initialize_session_state()

# Global Theme setup
theme_choice = st.session_state.get("theme_selection_box", "cloud_fusion")
if theme_choice not in THEMES:
    theme_choice = "cloud_fusion"
active_theme = THEMES[theme_choice]

# Hero Background Prep
hero_base64 = None
try:
    hero_base64 = get_base64_bin_file("images/hero_bg.png")
except:
    pass

# CSS Injection
st.markdown(get_main_css(active_theme, hero_base64), unsafe_allow_html=True)

def main():
    if st.session_state.page == "auth":
        render_auth_page()
        return

    # Sidebar Rendering
    render_sidebar()

    # Dynamic CSS injection based on active theme (reactivity)
    st.markdown(f"""
    <style>
        :root {{
            --text-primary: {active_theme['text']};
            --text-secondary: {active_theme['text_muted']};
            --accent: {active_theme['accent']};
            --accent-secondary: {active_theme['accent_secondary']};
            --bg: {active_theme['bg']};
            --panel: {active_theme['panel']};
            --border: {active_theme['border']};
        }}
        .stApp {{
            background:
                radial-gradient(ellipse at 10% 20%, rgba(186, 230, 253, 0.55) 0%, transparent 55%),
                radial-gradient(ellipse at 90% 80%, rgba(147, 197, 253, 0.45) 0%, transparent 55%),
                linear-gradient(160deg, #f0f9ff 0%, #e0f2fe 50%, #bfdbfe 100%) !important;
            background-attachment: fixed !important;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Hero Section - OneSchool Style
    st.markdown(f"""
    <div class="hero-container reveal">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1 class="hero-title reveal-delay-1">Master Every Tongue</h1>
            <p class="hero-subtitle reveal-delay-2">Experience the future of translation with Linguistix. Seamless, intelligent, and beautifully crafted for global connectivity.</p>
            <div class="reveal-delay-3" style="display: flex; gap: 15px; justify-content: center;">
                <a href="#translator" style="text-decoration: none;">
                    <div style="background: {active_theme['accent']}; color: white; padding: 12px 40px; border-radius: 50px; font-weight: 800; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 10px 30px {active_theme['accent']}40;">
                        Start Translating
                    </div>
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Header Section (Now more like a sub-header or title)
    st.markdown('<div class="reveal reveal-delay-2">', unsafe_allow_html=True)
    h_col1, h_col2 = st.columns([3, 1], gap="medium")
    with h_col1:
        st.markdown('<h1 style="text-align:left !important; margin-bottom:4px; margin-top:0; padding:0; font-weight:900; font-size:42px; letter-spacing:-1.5px;">Workspace</h1>', unsafe_allow_html=True)
        st.markdown("<p style='text-align:left !important; opacity:0.65; font-size:13px; margin:0; padding:0; margin-top:-2px; color:var(--text-secondary) !important;'>Everything you need, in one place.</p>", unsafe_allow_html=True)
    with h_col2:
        st.markdown("<div class='auth-btn' style='text-align:right; padding-top:4px;'>", unsafe_allow_html=True)
        if st.session_state.authenticated:
            col_profile, col_logout = st.columns([2, 1])
            with col_profile:
                if st.button(f"👤 {st.session_state.username}", key="nav_profile_btn", use_container_width=True):
                    st.session_state.show_dashboard = True
                    st.rerun()
            with col_logout:
                if st.button("Logout", key="nav_logout_btn", use_container_width=True):
                    st.session_state.authenticated = False
                    st.session_state.username = None
                    st.session_state.show_dashboard = False
                    st.session_state.history = []
                    st.session_state.favorites = []
                    st.session_state.phrasebook = []
                    st.rerun()
        else:
            if st.button("🔑 Login / Sign Up", key="nav_login_btn"):
                st.session_state.page = "auth"
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()

    # Tabs definition
    target_options = [l for l in SUPPORTED_LANGS.keys() if l != "auto"]
    tab_list = ["Translator", "🤝 Conversation", "Dictionary", "📲 Offline Hub"]
    if st.session_state.authenticated:
        tab_list += ["📸 Image Translate", "📄 Doc Translate", "🧩 Fun Zone"]
    else:
        tab_list += ["🔐 Image Translate", "🔐 Doc Translate", "🧩 Fun Zone"]

    tabs = st.tabs(tab_list)
    
    with tabs[0]:
        render_translator(target_options, create_pdf)
    with tabs[1]:
        render_conversation(target_options)
    with tabs[2]:
        render_dictionary(target_options)
    with tabs[3]:
        render_offline_hub()
    with tabs[4]:
        render_image_translate(target_options, create_pdf)
    with tabs[5]:
        render_doc_translate(target_options, create_pdf)
    with tabs[6]:
        render_fun_zone(render_word_games)

    # Dashboard Modal
    if st.session_state.show_dashboard and st.session_state.authenticated:
        show_dashboard_modal()

    # Footer Section
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.divider()
    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        st.markdown("**Your World, Translated.**")
        st.caption("Empowering global dialogue.")
    with f_col2:
        st.markdown("**Crafted for Clarity.**")
        st.caption("Clean code. Clean design.")
    with f_col3:
        st.markdown("**Always Evolving.**")
        st.caption("v1.0.0 | © 2026 Linguistix")

if __name__ == "__main__":
    main()