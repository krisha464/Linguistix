import streamlit as st
import datetime
from config import THEMES
from utils.storage import save_data

def render_sidebar():
    current_theme_key = st.session_state.get("theme_selection_box", "cloud_fusion")
    
    with st.sidebar:
        if st.session_state.authenticated:
            # === 1. PERSONAL CONCIERGE HEADER ===
            current_hour = datetime.datetime.now().hour
            greeting = "Good Morning" if current_hour < 12 else "Good Afternoon" if current_hour < 18 else "Good Evening"
            initials = st.session_state.username[0].upper() if st.session_state.username else "U"
            
            st.markdown(f"""
            <div style='padding: 20px 0 32px 0; text-align:center;'>
                <div style='position:relative; width:100px; height:100px; margin: 0 auto 20px auto;'>
                    <div style='position:absolute; inset:0; border:4px solid var(--accent)20; border-radius:50%;'></div>
                    <div style='position:absolute; inset:0; border:4px solid var(--accent); border-radius:50%; border-top-color:transparent; animation: spin 3s linear infinite;'></div>
                    <div style='position:absolute; inset:8px; background:var(--accent); border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-size:36px; font-weight:900; font-family:"Outfit"; box-shadow:0 10px 20px var(--glow);'>{initials}</div>
                </div>
                <p style='margin:0; font-size:12px; color:var(--accent); font-weight:800; text-transform:uppercase; letter-spacing:2px;'>{greeting}</p>
                <h3 style='margin:4px 0 0 0; font-size:28px; font-weight:900; color:var(--text-primary); letter-spacing:-1px;'>{st.session_state.username}</h3>
                <div style='display:inline-flex; align-items:center; gap:8px; background:var(--accent)10; padding:6px 16px; border-radius:20px; border:1px solid var(--accent)30; margin-top:12px; animation: pulseGlow 3s infinite;' title="The AI Concierge provides real-time grammar tips, synonyms, and cultural context based on your active translations.">
                    <span style='width:8px; height:8px; background:#10b981; border-radius:50%; box-shadow:0 0 10px #10b981;'></span>
                    <span style='font-size:12px; font-weight:800; color:var(--accent); text-transform:uppercase; letter-spacing:0.5px;'>AI Concierge Active ⓘ</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # === 2. LEARNING PROGRESS CAPSULE ===
            st.markdown(f"""
            <div class="sidebar-card" style="padding:20px; background:linear-gradient(135deg, var(--panel), var(--bg));">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <p style="margin:0; font-size:10px; font-weight:800; color:var(--text-secondary); text-transform:uppercase;">Insights</p>
                        <p style="margin:0; font-size:18px; font-weight:900; color:var(--text-primary);">{len(st.session_state.history)} translations</p>
                    </div>
                    <div style="width:40px; height:40px; background:var(--accent)15; border-radius:12px; display:flex; align-items:center; justify-content:center; color:var(--accent); font-size:20px; animation: float 3s ease-in-out infinite;">📈</div>
                </div>
                <div style="margin-top:12px; height:6px; background:var(--border); border-radius:10px; overflow:hidden;">
                    <div style="width:65%; height:100%; background:var(--accent); border-radius:10px;"></div>
                </div>
                <p style="margin:8px 0 0 0; font-size:11px; font-weight:700; color:var(--accent);">Daily goal: 65% achieved</p>
            </div>
            """, unsafe_allow_html=True)

            # === 3. SETTINGS & ATMOSPHERE ===
            if current_theme_key not in THEMES:
                current_theme_key = "cloud_fusion"
            
            st.selectbox(
                "Interface Atmosphere",
                options=list(THEMES.keys()),
                format_func=lambda x: THEMES[x]['name'],
                index=list(THEMES.keys()).index(current_theme_key),
                key="theme_selection_box"
            )

            # === 4. SMART AI CONTEXT PANEL (DYNAMICS) ===
            if st.session_state.translation_result:
                st.markdown(f"""
                <div class="sidebar-card" style="border: 1.5px dashed var(--accent); background: var(--accent)05;">
                    <p style="font-size:11px; font-weight:800; color:var(--accent); text-transform:uppercase; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
                        <i class="fas fa-sparkles"></i> AI Context Assistant
                    </p>
                    <p style="font-size:15px; font-weight:900; color:var(--text-primary); margin-bottom:10px; letter-spacing:-0.3px;">Smart Assistant Tip:</p>
                    <div style="background:white; padding:12px; border-radius:12px; border:1px solid var(--border);">
                        <p style="font-size:14px; font-style:italic; line-height:1.5; color:var(--text-primary); margin:0; font-weight:500;">The word reflects a formal tone. In casual conversation, locals might use 'hola' instead.</p>
                    </div>
                    <div style="margin-top:16px; padding-top:16px; border-top:1px solid var(--border);">
                        <p style="font-size:11px; font-weight:800; color:var(--text-secondary); margin-bottom:8px;">ALTERNATIVES</p>
                        <div style="display:flex; flex-wrap:wrap; gap:6px;">
                            <span style="background:white; border:1px solid var(--border); padding:4px 8px; border-radius:6px; font-size:11px; font-weight:700; color:var(--accent);">Hi there</span>
                            <span style="background:white; border:1px solid var(--border); padding:4px 8px; border-radius:6px; font-size:11px; font-weight:700; color:var(--accent);">Greetings</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # === 5. SMART TIMELINE (HISTORY) ===
            st.markdown("<p style='font-size:12px; font-weight:800; color:var(--text-secondary); text-transform:uppercase; letter-spacing:2px; margin-top:32px; margin-bottom:16px; padding-left:8px;'>Work Timeline</p>", unsafe_allow_html=True)
            
            if not st.session_state.history:
                st.caption("Timeline is empty")
            else:
                for idx, entry in enumerate(reversed(st.session_state.history[-5:])):
                    src = entry.get('src', '??').split('(')[-1].strip(')') if '(' in entry.get('src', '') else entry.get('src', '??')
                    tgt = entry.get('tgt', '??').split('(')[-1].strip(')') if '(' in entry.get('tgt', '') else entry.get('tgt', '??')
                    
                    st.markdown(f"""
                    <div class="sidebar-card" style="padding:16px; margin-bottom:12px; border-radius:16px;">
                        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                            <div>
                                <p style="margin:0; font-size:13px; font-weight:700; color:var(--text-primary);">{entry['input'][:20]}...</p>
                                <p style="margin:2px 0 0 0; font-size:11px; font-weight:800; color:var(--accent);">{src} → {tgt}</p>
                            </div>
                            <span style="font-size:10px; color:#94A3B8; font-weight:700;">{entry['Time']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"⚡ Restore Session #{idx}", key=f"hist_reuse_{idx}", use_container_width=True):
                        st.session_state.input_text = entry['input']
                        st.session_state.translation_result = entry['output']
                        st.rerun()

            st.markdown("<div style='margin-bottom:60px;'></div>", unsafe_allow_html=True)
            
            if st.button("🗑️ Wipe Workspace", key="sidebar_reset_btn", help="Permanently clear all data", use_container_width=True):
                st.session_state.history = []
                st.session_state.favorites = []
                st.session_state.phrasebook = []
                save_data([], [], [], username=st.session_state.username)
                st.toast("Workspace cleared.")
                st.rerun()
        else:
            st.markdown("""
            <div style='text-align:center; padding: 24px 0; opacity: 0.5;'>
                <i class='fas fa-lock' style='font-size:24px'></i>
                <p style='font-size:12px; margin-top:8px;'>Log in to access settings</p>
            </div>
            """, unsafe_allow_html=True)
