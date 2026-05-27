import streamlit as st
import time
from utils.storage import load_users, verify_password, load_data, hash_password, save_users, find_user, get_remembered_user, set_remember_me
import base64
import os

def render_auth_page():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Sora:wght@800&display=swap');

    /* ── PAGE BACKGROUND: Neutral Light Orange ── */
    .stApp {
        background: #FFFBF5 !important;
        font-family: 'Poppins', 'Inter', sans-serif !important;
        overflow-x: hidden;
    }
    }
    @keyframes particleFloat {
        0% { transform: translate(0, 0); opacity: 0; }
        50% { opacity: 0.5; }
        100% { transform: translate(var(--tw), var(--th)); opacity: 0; }
    }

    /* ── TRANSPARENT MAIN CONTAINER ── */
    .stMainBlockContainer {
        background: transparent !important;
        padding: 1rem 2rem !important;
        max-width: 1400px !important;
        position: relative;
        z-index: 1;
    }
    [data-testid="stSidebar"] { display: none !important; }

    /* ── PAGE FADE-IN ── */
    .stMainBlockContainer > div {
        animation: authFadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    @keyframes authFadeIn {
        from { opacity: 0; transform: translateY(40px); filter: blur(10px); }
        to   { opacity: 1; transform: translateY(0); filter: blur(0px); }
    }

    /* ── AI BADGE ── */
    .ai-badge {
        background: rgba(59, 130, 246, 0.05);
        color: #3B82F6;
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 0.65rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        border: 1px solid rgba(59, 130, 246, 0.2);
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 8px;
    }

    /* ── INPUTS: Light Blue Fill + Dark Blue Border ── */
    .auth-card .stTextInput input, .stTextInput input {
        background: #F0F7FF !important;
        border: 1.5px solid #1E3A8A !important;
        color: #1E3A8A !important;
        border-radius: 10px !important;
        padding: 8px 12px !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
        box-shadow: none !important;
    }
    .auth-card .stTextInput input:focus, .stTextInput input:focus {
        background: #EBF5FF !important;
        border-color: #2563EB !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
    }
    .auth-card label p, .stTextInput label p {
        color: #475569 !important;
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        text-transform: none !important;
        margin-bottom: 6px !important;
    }

    /* ── PILL TOGGLE ACTIVE STATES ── */
    .active-pill button {
        background: #F0F7FF !important;
        color: #1E3A8A !important;
        border: 1.5px solid #1E3A8A !important;
        box-shadow: 0 4px 12px rgba(30, 58, 138, 0.1) !important;
        font-weight: 700 !important;
    }
    .inactive-pill button {
        background: transparent !important;
        color: #64748B !important;
        border: 1px solid #CBD5E1 !important;
    }
    .inactive-pill button:hover {
        border-color: #3B82F6 !important;
        color: #3B82F6 !important;
    }

    /* ── AUTH BUTTON ── */
    /* ── AUTH BUTTON: Light Blue Fill + Dark Blue Border ── */
    .stButton button[kind="primary"] {
        background: #F0F7FF !important;
        color: #1E3A8A !important;
        border: 2px solid #1E3A8A !important;
        border-radius: 12px !important;
        padding: 1rem 2.5rem !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        letter-spacing: 0.5px !important;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        box-shadow: 0 4px 10px rgba(30, 58, 138, 0.1) !important;
    }
    .stButton button[kind="primary"]:hover {
        background: #EBF5FF !important;
        transform: translateY(-3px) scale(1.01) !important;
        box-shadow: 0 8px 16px rgba(30, 58, 138, 0.15) !important;
        border-color: #2563EB !important;
        color: #2563EB !important;
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
    
    @keyframes holographic {
        0% { opacity: 0.3; transform: translateX(-100%); }
        50% { opacity: 0.5; transform: translateX(100%); }
        100% { opacity: 0.3; transform: translateX(-100%); }
    }
    .ar-effect {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.2), transparent);
        animation: holographic 4s infinite linear;
        pointer-events: none;
        z-index: 2;
        mix-blend-mode: overlay;
    }
    .floating-robot {
        animation: floatRobot 6s ease-in-out infinite;
        position: relative;
        perspective: 1000px;
    }
    .floating-robot img {
        border: 2px solid #0F172A;
        box-shadow: 0 30px 60px rgba(59, 130, 246, 0.2) !important;
        border-radius: 20px;
        transition: all 0.5s ease;
    }
    .floating-robot:hover img {
        transform: rotateY(10deg) rotateX(5deg);
        box-shadow: 0 40px 80px rgba(59, 130, 246, 0.4) !important;
    }

    .particle {
        position: absolute;
        background: rgba(59, 130, 246, 0.2);
        border-radius: 50%;
        pointer-events: none;
        animation: particleFloat 10s infinite linear;
        z-index: -1;
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

    /* ── TEXT LINK STYLE ── */
    .text-link-btn .stButton button {
        background: transparent !important;
        color: #3B82F6 !important;
        border: none !important;
        padding: 0 !important;
        height: auto !important;
        line-height: inherit !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        text-decoration: none !important;
        box-shadow: none !important;
    }
    .text-link-btn .stButton button:hover {
        color: #2563EB !important;
        text-decoration: underline !important;
    }
    .orange-link-btn .stButton button {
        color: #EA580C !important;
    }
    .orange-link-btn .stButton button:hover {
        color: #C2410C !important;
        text-decoration: underline !important;
    }

    /* ── CUSTOM CHECKBOX ── */
    [data-testid="stCheckbox"] label span {
        color: #0F172A !important;
        font-weight: 600 !important;
    }
    [data-testid="stCheckbox"] div[role="checkbox"] {
        border-color: #3B82F6 !important;
        background-color: white !important;
    }
    [data-testid="stCheckbox"] div[role="checkbox"][aria-checked="true"] {
        background-color: #3B82F6 !important;
    }

    /* ── NO FORM CARD ── */
    .glass-card [data-testid="column"]:last-child > div:first-child {
        background: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        padding: 10px !important;
        box-shadow: none !important;
        max-width: 440px !important;
        margin: auto !important;
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

    .welcome-text {
        color: #FF5000 !important;
        font-weight: 800 !important;
        font-size: 2.2rem !important;
        margin: 0 !important;
        letter-spacing: -0.5px !important;
        text-align: center !important;
    }

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

    # === TOP: LOGO & TAGLINE ===
    st.markdown("""
<div style='text-align:center; animation: authFadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) both; margin-bottom:15px; position:relative;'>
    <div class="particle" style="--tw:100px; --th:-150px; width:12px; height:12px; top:20%; left:10%;"></div>
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@800&display=swap');
@keyframes brandShimmer {
    0% { background-position: -200% center; }
    100% { background-position: 200% center; }
}
.catchy-brand {
    background: linear-gradient(90deg, #0F172A, #3B82F6, #0F172A);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: brandShimmer 5s linear infinite;
    font-family: 'Sora', sans-serif !important;
    font-size: 72px !important;
    font-weight: 800 !important;
    letter-spacing: -4px !important;
    line-height: 1 !important;
    margin-bottom: 0px !important;
    display: inline-block;
    font-style: italic;
    transform: skewX(-2deg);
}
.special-x {
    color: #3B82F6 !important;
    -webkit-text-fill-color: #3B82F6 !important;
    font-size: 80px !important;
    margin-left: -5px;
    filter: drop-shadow(0 0 15px rgba(59, 130, 246, 0.4));
    position: relative;
    display: inline-block;
}
.special-x::after {
    content: '✦';
    position: absolute;
    top: -10px;
    right: -15px;
    font-size: 24px;
    background: linear-gradient(135deg, #3B82F6, #60A5FA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: pulseHeart 2s infinite;
}
@keyframes pulseHeart {
    0%, 100% { transform: scale(1); opacity: 0.8; }
    50% { transform: scale(1.2); opacity: 1; }
}
</style>
<div class="ai-badge">✨ THE FUTURE OF AI 🚀</div>
<h1 class="catchy-brand">LinguistiX</span>✦</h1> 
<p style="color:#475569 !important; font-size:20px !important; font-weight:600 !important; margin-top:0px !important; letter-spacing:0px;">Your World, Seamlessly Translated 🌎</p>
</div>
""", unsafe_allow_html=True)

    # === MIDDLE: ILLUSTRATION & GLASS CARD ===
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    info_col, spacer_col, form_col = st.columns([1, 0.2, 1.2], gap="large")

    with info_col:
        # ── LEFT SIDE: WELCOME + ILLUSTRATION ──
        st.markdown("""
<div style='margin-bottom:20px;'>
    <h3 class='welcome-text'>Welcome back 👋</h3>
</div>
""", unsafe_allow_html=True)
        
        # Centered Illustration - scaling with container
        img_path = os.path.join("images", "login_image.png")
        if os.path.exists(img_path):
            with open(img_path, "rb") as f:
                data = base64.b64encode(f.read()).decode()
            st.markdown(f"""
            <div class="floating-robot" style='text-align:center;'>
                <img src="data:image/png;base64,{data}" style="width:95%; border-radius:20px;">
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Login image not found.")

    with form_col:
        # ── RIGHT SIDE: TAGLINE + AUTH FORM ──
        st.markdown("""
<div style='margin-bottom:20px;'>
    <p style='color:#fc9409; font-size:1.1rem; margin:0; line-height:1.4; font-weight:700;'>Sign in to your AI workspace ⚡</p>
</div>
""", unsafe_allow_html=True)

        # ── Pill Toggle via session state buttons ──
        if "auth_tab" not in st.session_state:
            remembered = get_remembered_user()
            if remembered:
                st.session_state.auth_tab = "login"
                st.session_state.prefill_user = remembered
            else:
                st.session_state.auth_tab = "login"
        
        active_tab = st.session_state.auth_tab

        # Pill row container (Optional: Hidden to reduce clutter as per link request, but keeping for now)
        tab_col1, tab_col2 = st.columns(2)
        with tab_col1:
            st.markdown(f'<div class="{"active-pill" if active_tab == "login" else "inactive-pill"}">', unsafe_allow_html=True)
            if st.button("🔓 Login", key="pill_login", use_container_width=True):
                st.session_state.auth_tab = "login"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with tab_col2:
            st.markdown(f'<div class="{"active-pill" if active_tab == "signup" else "inactive-pill"}">', unsafe_allow_html=True)
            if st.button("✍️ Sign Up", key="pill_signup", use_container_width=True):
                st.session_state.auth_tab = "signup"
                st.rerun()
            st.markdown('</div></div>', unsafe_allow_html=True)
        # Form setup section follows below

        # ── Form ──
        users = load_users()
        if st.session_state.auth_tab == "login":
            u_in = st.text_input("👤 Username or Email", placeholder="Enter username", key="page_u_in")
            p_in = st.text_input("🔑 Password", type="password", placeholder="••••••••", key="page_p_in")
            
            st.markdown("<div style='margin-bottom: 12px;'>", unsafe_allow_html=True)
            col_link1, col_link2 = st.columns([1, 1])
            with col_link1:
                st.markdown("<div class='text-link-btn'>", unsafe_allow_html=True)
                if st.button("Forgot Password?", key="forgot_link_btn"):
                    st.session_state.auth_tab = "forgot"
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)
            with col_link2:
                st.markdown("<div class='text-link-btn orange-link-btn' style='text-align: right;'>", unsafe_allow_html=True)
                if st.button("New to Linguistix?", key="go_to_signup_link"):
                    st.session_state.auth_tab = "signup"
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🔓 Sign In", width='stretch', type="primary", key="sign_in_btn"):
                if not u_in or not p_in:
                    st.error("⚠️ Please enter both username and password")
                else:
                    with st.spinner("Authenticating..."):
                        time.sleep(0.5)
                        username, user_data = find_user(u_in, users)
                        if user_data and verify_password(p_in, user_data["password"]):
                            st.session_state.authenticated = True
                            st.session_state.username = username
                            u_data = load_data(username)
                            st.session_state.history = u_data.get("history", [])
                            st.session_state.favorites = u_data.get("favorites", [])
                            st.session_state.phrasebook = u_data.get("phrasebook", [])
                            st.session_state.page = "main"
                            st.toast(f"✅ Welcome back, {username}!", icon="🎉")
                            time.sleep(0.5)
                            st.rerun()
                        else:
                            st.error("❌ Invalid credentials. Please check your username/password.")
        
        elif st.session_state.auth_tab == "signup":
            nu_in = st.text_input("👤 Choose a Username", placeholder="e.g. linguist_pro", key="page_nu_in")
            em_in = st.text_input("📧 Email Address", placeholder="name@example.com", key="page_em_in")
            np_in = st.text_input("🔐 Create a Password", type="password", placeholder="Min. 6 characters", key="page_np_in")
            cp_in = st.text_input("✅ Confirm Password", type="password", placeholder="Repeat password", key="page_cp_in")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚀 Create Account", width='stretch', type="primary", key="create_acc_btn"):
                if nu_in in users:
                    st.error("Username already taken")
                elif any(u["email"] == em_in for u in users.values() if isinstance(u, dict)):
                    st.error("Email already registered")
                elif np_in != cp_in:
                    st.error("Passwords do not match")
                elif len(nu_in) < 3 or len(np_in) < 6 or "@" not in em_in:
                    st.warning("Please fill all fields correctly. Password min 6 chars.")
                else:
                    users[nu_in] = {"password": hash_password(np_in), "email": em_in}
                    save_users(users)
                    st.toast("Account created successfully!", icon="🚀")
                    st.session_state.auth_tab = "login"
                    st.rerun()

        elif st.session_state.auth_tab == "forgot":
            st.markdown("### Reset Password")
            f_u_in = st.text_input("Username or Email", placeholder="Enter your account info", key="forgot_u_in")
            f_p_in = st.text_input("New Password", type="password", placeholder="••••••••", key="forgot_p_in")
            f_cp_in = st.text_input("Confirm New Password", type="password", placeholder="••••••••", key="forgot_cp_in")
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button("Reset Password", type="primary", use_container_width=True):
                    username, user_data = find_user(f_u_in, users)
                    if not user_data:
                        st.error("User not found")
                    elif f_p_in != f_cp_in:
                        st.error("Passwords do not match")
                    elif len(f_p_in) < 6:
                        st.error("Password too short")
                    else:
                        users[username]["password"] = hash_password(f_p_in)
                        save_users(users)
                        st.success("Password updated! Please login.")
                        st.session_state.auth_tab = "login"
                        time.sleep(1.5)
                        st.rerun()
            with col_b2:
                if st.button("Back to Login", key="back_to_login_btn", use_container_width=True):
                    st.session_state.auth_tab = "login"
                    st.rerun()
