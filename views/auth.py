import streamlit as st
import time
from utils.storage import load_users, verify_password, load_data, hash_password, save_users

def render_auth_page():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    /* ── PAGE BACKGROUND: simple clean light blue ── */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%) !important;
        font-family: 'Poppins', 'Inter', sans-serif !important;
        overflow-x: hidden;
    }
    .stApp::before {
        content: '';
        position: fixed;
        top: -30%;  left: 40%;
        width: 800px; height: 800px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, transparent 70%);
        animation: floatOrb1 12s ease-in-out infinite alternate;
        pointer-events: none;
        z-index: 0;
        filter: blur(40px);
    }
    .stApp::after {
        content: '';
        position: fixed;
        bottom: -20%;  left: -10%;
        width: 600px; height: 600px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(96, 165, 250, 0.12) 0%, transparent 70%);
        animation: floatOrb2 15s ease-in-out infinite alternate;
        pointer-events: none;
        z-index: 0;
        filter: blur(50px);
    }
    
    /* Additional Floating Orb */
    .orb-3 {
        position: fixed;
        top: 20%;  right: -5%;
        width: 400px; height: 400px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(147, 197, 253, 0.08) 0%, transparent 70%);
        animation: floatOrb1 10s ease-in-out infinite alternate-reverse;
        pointer-events: none;
        z-index: 0;
        filter: blur(30px);
    }

    @keyframes floatOrb1 {
        from { transform: translate(0, 0) scale(1); }
        to   { transform: translate(-60px, 40px) scale(1.1); }
    }
    @keyframes floatOrb2 {
        from { transform: translate(0, 0) scale(1); }
        to   { transform: translate(50px, -40px) scale(1.15); }
    }

    /* ── TRANSPARENT MAIN CONTAINER ── */
    .stMainBlockContainer {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
        backdrop-filter: none !important;
        padding: 1.5rem 2rem !important;
        max-width: 1240px !important;
        position: relative;
        z-index: 1;
    }
    [data-testid="stSidebar"] { display: none !important; }

    /* ── PAGE FADE-IN ── */
    .stMainBlockContainer > div {
        animation: authFadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    @keyframes authFadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ── AI BADGE ── */
    .ai-badge {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(96, 165, 250, 0.1));
        color: #2563EB;
        padding: 8px 16px;
        border-radius: 50px;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: 1px solid rgba(59, 130, 246, 0.3);
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.1);
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 16px;
    }
    .ai-badge::before {
        content: '';
        width: 6px; height: 6px;
        background: #3B82F6;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 8px #3B82F6;
        animation: pulseHeart 2s infinite;
    }
    @keyframes pulseHeart {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.5); opacity: 0.5; }
        100% { transform: scale(1); opacity: 1; }
    }

    /* ── INPUTS ── */
    .auth-card .stTextInput input, .stTextInput input {
        background: white !important;
        border: 2px solid #3B82F6 !important;
        color: #0F172A !important;
        border-radius: 16px !important;
        padding: 20px 24px !important;
        font-size: 1.05rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.08) !important;
        letter-spacing: 0.3px !important;
        width: 100% !important;
    }
    .auth-card .stTextInput input:focus, .stTextInput input:focus {
        background: white !important;
        border-color: #2563EB !important;
        box-shadow: 
            0 0 0 4px rgba(37, 99, 235, 0.15),
            0 8px 24px rgba(37, 99, 235, 0.2) !important;
        outline: none !important;
        transform: translateY(-2px);
    }
    .auth-card .stTextInput input::placeholder, .stTextInput input::placeholder {
        color: #64748B !important;
        opacity: 0.9 !important;
    }
    .auth-card label p, .stTextInput label p {
        color: #1E40AF !important;
        font-size: 0.8rem !important;
        font-weight: 800 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        margin-bottom: 10px !important;
    }

    /* ── AUTH BUTTON ── */
    .stButton button[kind="primary"] {
        background: linear-gradient(135deg, #2563EB, #3B82F6, #2563EB) !important;
        background-size: 200% 200% !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 1rem 2.5rem !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        letter-spacing: 0.8px !important;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }
    .stButton button[kind="primary"]:hover {
        transform: translateY(-5px) scale(1.02) !important;
        box-shadow: 0 20px 40px rgba(37, 99, 235, 0.5) !important;
    }
    .stButton button[kind="primary"]:active {
        transform: translateY(-2px) scale(0.98) !important;
    }

    /* ── BACK BUTTON ── */
    .back-btn .stButton button {
        background: white !important;
        color: #3B82F6 !important;
        border: 1px solid rgba(59, 130, 246, 0.2) !important;
        border-radius: 50px !important;
        padding: 0.5rem 1.4rem !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    .back-btn .stButton button:hover {
        background: rgba(59, 130, 246, 0.1) !important;
        border-color: rgba(59, 130, 246, 0.4) !important;
        transform: translateX(-4px) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1) !important;
    }

    /* ── FEATURE BLOCKS ── */
    .feat-icon {
        width: 44px; height: 44px;
        border-radius: 12px;
        display: inline-flex; align-items: center; justify-content: center;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .feat-icon.purple { background: rgba(139,92,246,0.18); box-shadow: 0 0 20px rgba(139,92,246,0.25); }
    .feat-icon.indigo { background: rgba(99,102,241,0.18);  box-shadow: 0 0 20px rgba(99,102,241,0.25); }
    .feat-icon.blue   { background: rgba(96,165,250,0.18);  box-shadow: 0 0 20px rgba(96,165,250,0.25); }

    /* ── TYPING ANIMATION ── */
    .typing-text::after {
        content: '|';
        animation: blink 0.8s infinite;
        color: #3B82F6;
    }
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    
    .product-preview-container {
        margin-top: 32px;
        position: relative;
        width: 100%;
        max-width: 360px;
        perspective: 1000px;
    }
    .product-preview {
        width: 100%;
        border-radius: 16px;
        border: 1px solid rgba(139, 92, 246, 0.3);
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.15);
        transform: rotateY(-15deg) rotateX(10deg);
        transition: all 0.5s ease;
        opacity: 0.85;
    }
    .product-preview:hover {
        transform: rotateY(0deg) rotateX(0deg) scale(1.05);
        opacity: 1;
        box-shadow: 0 30px 60px rgba(139, 92, 246, 0.2);
    }

    /* ── FEATURE BLOCKS ── */
    .forgot-link {
        text-align: right;
        margin-top: 0;
        margin-bottom: 16px;
    }
    .forgot-link a {
        color: #3B82F6 !important;
        font-size: 0.75rem;
        text-decoration: none;
        font-weight: 600;
        opacity: 0.8;
    }
    
    .caps-warning {
        color: #F87171;
        font-size: 0.7rem;
        font-weight: 600;
        margin-top: 8px;
        display: none;
    }

    /* ── RIGHT COLUMN CARD ── */
    [data-testid="column"]:last-child > div:first-child {
        background: rgba(255, 255, 255, 0.85) !important;
        border: 1px solid rgba(59, 130, 246, 0.15) !important;
        border-radius: 32px !important;
        padding: 32px !important;
        box-shadow: 
            0 32px 64px -12px rgba(59, 130, 246, 0.08),
            0 0 0 1px rgba(255, 255, 255, 0.03) inset !important;
        backdrop-filter: blur(40px) !important;
        position: relative !important;
    }

    /* ── RESPONSIVENESS ── */
    @media (max-width: 768px) {
        .brand-title { font-size: 36px !important; text-align: center !important; }
        [data-testid="column"] { width: 100% !important; flex: 1 1 100% !important; }
        .feat-icon { width: 36px; height: 36px; }
        [data-testid="column"]:last-child > div:first-child { padding: 24px !important; }
    }

    /* ── HIDE empty markdown divs ── */
    .stMarkdown:empty { display:none !important; }

    </style>
    <div class="orb-3"></div>
    """, unsafe_allow_html=True)

    # === HEADER / BRANDING ROW ===
    back_col, _ = st.columns([1, 3])
    with back_col:
        st.markdown("<div class='back-btn'>", unsafe_allow_html=True)
        if st.button("⬅️ Back", key="back_to_main"):
            st.session_state.page = "main"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # === HEADER: BRANDING & HIGHLIGHTS ===
    st.markdown(f"""
<div style='text-align:center; animation: authFadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) both; margin-bottom:48px;'>
<style>
@keyframes brandShimmer {{
    0% {{ background-position: -200% center; }}
    100% {{ background-position: 200% center; }}
}}
.catchy-brand {{
    background: linear-gradient(90deg, #1E293B, #3B82F6, #1E293B);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: brandShimmer 5s linear infinite;
    font-size: 80px !important;
    font-weight: 900 !important;
    letter-spacing: -4px !important;
    line-height: 1 !important;
    margin-bottom: 8px !important;
    display: inline-block;
    filter: drop-shadow(0 4px 8px rgba(59, 130, 246, 0.1));
}}
</style>
<div class="ai-badge" style='margin-bottom:16px;'>✨ THE FUTURE OF TRANSLATION</div>
<h1 class="catchy-brand">Linguistix</h1>
<p style="color:#3B82F6 !important; font-size:22px !important; font-weight:700 !important; margin-bottom:32px !important; opacity:0.8; letter-spacing:1px;">Your World, Translated.</p>

<div style='display:flex; justify-content:center; gap:40px; flex-wrap:wrap; margin-top:24px;'>
<div style='display:flex; align-items:center; gap:12px;'>
<div class="feat-icon blue" style="background:rgba(59,130,246,0.1) !important; width:40px; height:40px; border-radius:10px; display:flex; align-items:center; justify-content:center;"><i class="fas fa-microphone-alt" style="color:#3B82F6; font-size:14px;"></i></div>
<div><b style="color:#1E293B !important; font-size:14px;">AI Voice Translation</b></div>
</div>
<div style='display:flex; align-items:center; gap:12px;'>
<div class="feat-icon blue" style="background:rgba(59,130,246,0.1) !important; width:40px; height:40px; border-radius:10px; display:flex; align-items:center; justify-content:center;"><i class="fas fa-camera" style="color:#3B82F6; font-size:14px;"></i></div>
<div><b style="color:#1E293B !important; font-size:14px;">Visual OCR & TR</b></div>
</div>
<div style='display:flex; align-items:center; gap:12px;'>
<div class="feat-icon blue" style="background:rgba(59,130,246,0.1) !important; width:40px; height:40px; border-radius:10px; display:flex; align-items:center; justify-content:center;"><i class="fas fa-brain" style="color:#3B82F6; font-size:14px;"></i></div>
<div><b style="color:#1E293B !important; font-size:14px;">Contextual Intelligence</b></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
    
    # === CONTENT: ILLUSTRATION & FORM ===
    info_col, spacer_col, form_col = st.columns([1, 0.2, 1.3], gap="large")

    with info_col:
        # Centered Illustration - scaling with container
        st.markdown("""
        <div style='text-align:center; padding-top:20px; margin-bottom: 20px;'>
            <img src="https://img.freepik.com/free-vector/global-connection-concept-illustration_114360-10118.jpg" style="width:100%; border-radius:20px;">
        </div>
        """, unsafe_allow_html=True)

    with form_col:
        # ── RIGHT SIDE: AUTH FORM ──
        st.markdown("""
<div style='margin-bottom:32px;'>
    <p style='color:#3B82F6; font-size:0.68rem; font-weight:800; letter-spacing:2.5px; text-transform:uppercase; margin:0 0 8px 0;'>✦ AI WORKSPACE</p>
    <h3 style='color:#000000; font-weight:700; font-size:1.6rem; margin:0 0 8px 0; letter-spacing:-0.5px;'>Welcome back 👋</h3>
    <p style='color:#475569; font-size:0.85rem; margin:0; line-height:1.5;'>Sign in to access your personal workspace</p>
</div>
""", unsafe_allow_html=True)

        # ── Pill Toggle via session state buttons ──
        if "auth_tab" not in st.session_state:
            st.session_state.auth_tab = "login"
        active_tab = st.session_state.auth_tab

        # Pill row container
        tab_col1, tab_col2 = st.columns(2)
        with tab_col1:
            if st.button("🔓 Login", key="pill_login", width='stretch'):
                st.session_state.auth_tab = "login"
                st.rerun()
        with tab_col2:
            if st.button("✍️ Sign Up", key="pill_signup", width='stretch'):
                st.session_state.auth_tab = "signup"
                st.rerun()
        # Form setup section follows below

        # ── Form ──
        users = load_users()
        if st.session_state.auth_tab == "login":
            u_in = st.text_input("Username", placeholder="Enter your username", key="page_u_in")
            p_in = st.text_input("Password", type="password", placeholder="••••••••", key="page_p_in")
            
            st.markdown("""
            <div class="forgot-link"><a href="#">Forgot password?</a></div>
            <div id="caps-warning" class="caps-warning"><i class="fas fa-exclamation-triangle"></i> Caps Lock is ON</div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
            
            # Loader logic
            if "is_authenticating" not in st.session_state:
                st.session_state.is_authenticating = False
            
            if st.button("🔓 Sign In", width='stretch', type="primary", key="sign_in_btn", disabled=st.session_state.is_authenticating):
                st.session_state.is_authenticating = True
                with st.spinner("Authenticating..."):
                    # Micro-delay for feel
                    time.sleep(0.8)
                    if u_in in users and verify_password(p_in, users[u_in]):
                        st.session_state.authenticated = True
                        st.session_state.username = u_in
                        u_data = load_data(u_in)
                        st.session_state.history = u_data.get("history", [])
                        st.session_state.favorites = u_data.get("favorites", [])
                        st.session_state.phrasebook = u_data.get("phrasebook", [])
                        st.session_state.page = "main"
                        st.session_state.is_authenticating = False
                        st.toast("✅ Welcome back, " + u_in + "!", icon="🎉")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.session_state.is_authenticating = False
                        st.error("❌ Invalid username or password")
        else:
            nu_in = st.text_input("Choose a Username", placeholder="e.g. linguist_pro", key="page_nu_in")
            np_in = st.text_input("Create a Password", type="password", placeholder="Min. 6 characters", key="page_np_in")
            
            # Password Strength
            strength = 0
            if len(np_in) >= 6: strength += 25
            if any(c.isupper() for c in np_in): strength += 25
            if any(c.isdigit() for c in np_in): strength += 25
            if any(c in "!@#$%^&*" for c in np_in): strength += 25
            
            strength_color = "#F87171" if strength < 50 else "#FBBF24" if strength < 100 else "#34D399"
            
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                <span style="font-size: 0.65rem; color: #64748B; font-weight: 600;">PASSWORD STRENGTH</span>
                <span style="font-size: 0.65rem; color: {strength_color}; font-weight: 700;">{ "Weak" if strength < 50 else "Medium" if strength < 100 else "Strong" }</span>
            </div>
            <div class="password-strength" style="display: block;">
                <div class="password-strength-fill" style="width: {strength}%; background: {strength_color};"></div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
            if st.button("🚀 Create Account", width='stretch', type="primary", key="create_acc_btn"):
                if nu_in in users:
                    st.error("Username already taken")
                elif len(nu_in) < 3 or len(np_in) < 6:
                    st.warning("Username (3+ chars) and Password (6+ chars) required.")
                else:
                    users[nu_in] = hash_password(np_in)
                    save_users(users)
                    st.toast("Account created successfully!", icon="🚀")
                    st.session_state.auth_tab = "login"
                    st.rerun()
