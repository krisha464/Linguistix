import streamlit as st

@st.dialog("📊 Mission Control", width="large")
def show_dashboard_modal():
    st.markdown(f"<p style='opacity:0.7;'>Welcome back, <b>{st.session_state.username}</b>! Here is your progress.</p>", unsafe_allow_html=True)
    
    dash_col1, dash_col2 = st.columns([1, 1], gap="large")
    
    with dash_col1:
        st.markdown("#### 🕒 Recent Activity")
        if not st.session_state.history:
            st.caption("No history yet.")
        else:
            activity_html = '<div class="roll-container">'
            for item in reversed(st.session_state.history[-10:]):
                t_str = item.get('Time', '00:00')
                src_str = item.get('src', 'N/A')
                tgt_str = item.get('tgt', 'N/A')
                in_str = item.get('input', '')[:40]
                out_str = item.get('output', '')[:40]

                activity_html += f'<div class="result-card roll-item" style="padding:15px !important; border-left: 4px solid var(--accent) !important; height: 160px; display:flex; flex-direction:column; justify-content:space-between;">'
                activity_html += f'<div><small style="opacity:0.6;">{t_str} | {src_str} ⮕ {tgt_str}</small><br>'
                activity_html += f'<div style="font-weight:700; font-size:14px; margin:4px 0;">{in_str}</div></div>'
                activity_html += f'<div style="color:var(--accent); font-weight:600; font-size:14px;">{out_str}</div>'
                activity_html += f'</div>'
            
            activity_html += '</div>'
            st.markdown(activity_html, unsafe_allow_html=True)

    with dash_col2:
        st.markdown("#### 📈 Your Stats")
        total_tr = len(st.session_state.history)
        fav_count = len(st.session_state.favorites)
        top_lang = "None"
        if total_tr > 0:
            langs_used = [item['tgt'] for item in st.session_state.history]
            top_lang = max(set(langs_used), key=langs_used.count)
            
        st.metric("Total Translations", total_tr)
        st.metric("Vocabulary Saved", fav_count)
        st.metric("Top Language", top_lang)
    
    if st.button("Close Dashboard"):
        st.session_state.show_dashboard = False
        st.rerun()
