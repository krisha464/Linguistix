def get_main_css(theme, hero_bg_base64=None):
    hero_bg_style = f"background-image: url(data:image/png;base64,{hero_bg_base64}); background-size: cover; background-position: center;" if hero_bg_base64 else ""
    return f"""

<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800&family=Inter:wght@400;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

    :root {{
        --text-primary: {theme['text']};
        --text-secondary: {theme['text_muted']};
        --text-inverse: {theme.get('text_inverse', '#ffffff')};
        --accent: {theme['accent']};
        --accent-secondary: {theme['accent_secondary']};
        --panel: {theme['panel']};
        --bg: {theme['bg']};
        --border: {theme['border']};
        --glow: {theme.get('glow', 'rgba(0,0,0,0.1)')};
        --font-heading: 'Outfit', sans-serif;
        --font-body: 'Inter', sans-serif;
    }}

    /* GLOBAL RESET - Clean and minimal */
    #MainMenu, footer, [data-testid="stDecoration"] {{visibility: hidden; display: none !important;}}
    
    header, [data-testid="stHeader"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
        height: 70px !important;
        transition: all 0.4s ease !important;
        z-index: 999999 !important;
    }}
    
    [data-testid="stHeader"] > div {{visibility: visible !important;}}
    
    /* ═══════════════════════════════════════════════════
       BACKGROUND - Premium Full-Page Background
    ═══════════════════════════════════════════════════ */
    .stApp {{
        background: 
            linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)),
            url(data:image/png;base64,{hero_bg_base64}) !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        color: var(--text-primary) !important;
        font-family: var(--font-body) !important;
        padding: 0 !important;
        margin: 0 !important;
    }}

    /* Force global text color with high specificity and readability */
    .stApp, .stApp p, .stApp span, .stApp label, .stApp .stMarkdown div, .stApp .stCaption,
    [data-testid="stWidgetLabel"] p, [data-testid="stHeader"] *, .stMarkdown p,
    .stSelectbox div, .stTextInput div, .stTextArea div {{
        color: var(--text-primary) !important;
    }}
    
    /* Input field text color stabilization */
    input, textarea, select {{
        color: var(--text-primary) !important;
    }}
    
    /* Ensure inputs have a theme-appropriate background */
    .stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] {{
        background: var(--panel) !important;
        color: var(--text-primary) !important;
        border: 1.5px solid var(--border) !important;
    }}

    .stTextInput input:focus, .stTextArea textarea:focus {{
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px var(--glow) !important;
    }}
    
    /* Ensure muted/secondary text is still using the correct variable */
    .secondary-text, [data-testid="stCaption"], .stCaption {{
        color: var(--text-secondary) !important;
        opacity: 0.8 !important;
    }}

    /* Sidebar - Soft Light Shade */
    [data-testid="stSidebar"] {{
        background-color: #F8FAFC !important;
        border-right: 1px solid var(--border) !important;
    }}
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {{
        color: var(--text-primary) !important;
    }}

    [data-testid="stSidebar"] [data-testid="stExpander"] > div:first-child,
    [data-testid="stSidebar"] [data-testid="stExpander"] > div:nth-child(2),
    [data-testid="stExpander"] {{
        background: #EFF6FF !important;
        border: 1.5px solid rgba(59, 130, 246, 0.15) !important;
        border-radius: 14px !important;
        color: #1E293B !important;
    }}

    /* Global Expander Header Fix */
    [data-testid="stExpander"] summary {{
        background: #EFF6FF !important;
        color: #1E293B !important;
        font-weight: 700 !important;
    }}

    [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"],
    .stSelectbox [data-baseweb="select"] {{
        background: var(--panel) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 14px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
    }}
    .stSelectbox [data-baseweb="select"] * {{
        background: transparent !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }}

    /* GLOBAL — Selectbox floating dropdown (FORCE LIGHT) */
    [data-baseweb="popover"], [role="listbox"], [data-baseweb="menu"] {{
        background: var(--panel) !important;
        border: 1px solid var(--border) !important;
        box-shadow: 0 10px 40px rgba(0,0,0,0.12) !important;
        border-radius: 12px !important;
    }}
    [role="option"], [data-baseweb="menu"] li {{
        background: var(--panel) !important;
        color: var(--text-primary) !important;
        padding: 10px 16px !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease !important;
    }}
    [role="option"]:hover, [data-baseweb="menu"] li:hover {{
        background: var(--accent)15 !important;
        color: var(--accent) !important;
    }}
    
    .result-card {{
        background: #FFFFFF !important;
        border: 1.5px solid rgba(59, 130, 246, 0.15) !important;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.06) !important;
        color: #1E293B !important;
        padding: 24px;
        border-radius: 20px;
    }}

    /* FILE UPLOADER - Comprehensive Cloud Fusion Pastel Styling */
    .stFileUploader section, 
    [data-testid="stFileUploadDropzone"], 
    .stFileUploader {{
        background: #F8FAFC !important;
        border: 2.2px dashed rgba(59, 130, 246, 0.25) !important;
        border-radius: 18px !important;
        transition: all 0.3s ease !important;
        color: #1E293B !important;
        padding: 24px !important;
        min-height: 120px !important;
    }}
    
    .stFileUploader section:hover, 
    [data-testid="stFileUploadDropzone"]:hover {{
        background: #EFF6FF !important;
        border-color: #2563EB !important;
        border-width: 2.5px !important;
        box-shadow: 0 8px 30px rgba(37, 99, 235, 0.12) !important;
        transform: translateY(-2px) !important;
    }}
    
    /* Force text/icon colors inside uploader dropzone only */
    [data-testid="stFileUploadDropzone"] * {{
        color: #1E293B !important;
        background: transparent !important;
        fill: #3B82F6 !important;
    }}

    /* Uploaded file name chip — must stay readable */
    [data-testid="stFileUploaderFile"],
    [data-testid="stFileUploaderFileName"],
    .stFileUploader [data-testid="stFileUploaderDeleteBtn"] ~ span,
    .stFileUploader li,
    .stFileUploader li span,
    .stFileUploader li p,
    [data-testid="stFileUploader"] li,
    [data-testid="stFileUploader"] li span,
    [data-testid="stFileUploader"] li p {{
        color: #1E293B !important;
        background: #FFFFFF !important;
    }}

    /* File name pill/chip wrapper */
    .stFileUploader [class*="fileInfo"],
    .stFileUploader [class*="UploadedFile"],
    [data-testid="stFileUploaderFile"] {{
        background: #FFFFFF !important;
        border: 1px solid rgba(59, 130, 246, 0.2) !important;
        border-radius: 10px !important;
        color: #1E293B !important;
        padding: 6px 12px !important;
    }}

    /* Filename text specifically */
    [data-testid="stFileUploaderFileName"] span,
    [data-testid="stFileUploaderFileName"] p,
    [data-testid="stFileUploaderFileName"] {{
        color: #1E293B !important;
        background: transparent !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }}
    
    /* Browse Button Inside Uploader specifically */
    .stFileUploader button, 
    [data-testid="stFileUploadDropzone"] button {{
        background: #FFFFFF !important;
        border: 1.5px solid rgba(59, 130, 246, 0.3) !important;
        border-radius: 12px !important;
        color: #3B82F6 !important;
        font-weight: 800 !important;
        padding: 10px 24px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02) !important;
    }}
    [role="option"][aria-selected="true"] {{
        background: {theme['accent']}22 !important;
        color: {theme['accent']} !important;
        font-weight: 700 !important;
    }}


    /* MAIN CONTAINER - Proper alignment and spacing */
    .stMainBlockContainer {{
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0.75rem 1.5rem 2rem 1.5rem !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
        width: 100% !important;
        max-width: 1400px !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        position: relative !important;
    }}

    /* MOBILE RESPONSIVE */
    @media (max-width: 768px) {{
        .stMainBlockContainer {{
            padding: 1rem 0.75rem !important;
        }}
        h1 {{ font-size: 32px !important; }}
        [data-testid="stHorizontalBlock"] {{
            flex-direction: column !important;
            gap: 0.5rem !important;
        }}
    }}

    /* ═══════════════════════════════════════════════════
       ANIMATIONS - OneSchool Style
    ═══════════════════════════════════════════════════ */
    @keyframes fadeInUp {{ 
        from {{ opacity: 0; transform: translateY(40px); }} 
        to {{ opacity: 1; transform: translateY(0); }} 
    }}
    @keyframes fadeInRight {{ 
        from {{ opacity: 0; transform: translateX(-30px); }} 
        to {{ opacity: 1; transform: translateX(0); }} 
    }}
    @keyframes scaleIn {{ 
        from {{ opacity: 0; transform: scale(0.95); }} 
        to {{ opacity: 1; transform: scale(1); }} 
    }}
    @keyframes globalShimmer {{ 
        0% {{ background-position: -100% center; }} 
        100% {{ background-position: 100% center; }} 
    }}
    @keyframes float {{ 
        0%, 100% {{ transform: translateY(0); }} 
        50% {{ transform: translateY(-10px); }} 
    }}

    .reveal {{
        animation: fadeInUp 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    }}

    .reveal-delay-1 {{ animation-delay: 0.1s; }}
    .reveal-delay-2 {{ animation-delay: 0.2s; }}
    .reveal-delay-3 {{ animation-delay: 0.3s; }}

    /* ═══════════════════════════════════════════════════
       HERO SECTION 
    ═══════════════════════════════════════════════════ */
    .hero-container {{
        position: relative;
        width: 100%;
        height: 500px;
        border-radius: 30px;
        overflow: hidden;
        margin-bottom: 50px;
        background: transparent !important;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    .hero-overlay {{
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 30% 50%, rgba(0,0,0,0.1), transparent),
                    linear-gradient(0deg, rgba(0,0,0,0.4) 0%, transparent 60%);
        z-index: 1;
    }}

    .hero-content {{
        position: relative;
        z-index: 2;
        padding: 40px;
        color: var(--text-primary) !important;
        max-width: 800px;
    }}

    .hero-title {{
        font-family: var(--font-heading) !important;
        font-size: 72px !important;
        font-weight: 800 !important;
        line-height: 1.1 !important;
        letter-spacing: -3px !important;
        margin-bottom: 20px !important;
        color: var(--text-primary) !important;
        text-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
    }}

    .hero-subtitle {{
        font-size: 20px !important;
        opacity: 0.8;
        font-weight: 600 !important;
        margin-bottom: 30px !important;
        color: var(--text-primary) !important;
    }}

    /* TYPOGRAPHY */
    h1 {{
        background: linear-gradient(90deg, var(--text-primary), var(--accent), var(--text-primary));
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: globalShimmer 5s linear infinite;
        font-family: var(--font-heading) !important;
        font-size: 64px !important;
        font-weight: 800 !important;
        letter-spacing: -2.5px !important;
        text-align: left !important;
        margin-bottom: 4px !important;
        margin-top: 0 !important;
    }}
    
    h2, h3, h4 {{
        color: var(--text-primary) !important;
        font-family: var(--font-heading) !important;
        font-weight: 800 !important;
        letter-spacing: -1px !important;
    }}
    
    .tagline {{
        text-align: left;
        color: var(--text-secondary);
        font-weight: 600;
        font-size: 15px;
        margin-bottom: 0;
        margin-top: 0;
        opacity: 0.75;
        letter-spacing: 0.2px;
    }}

    /* LAYOUT SECTIONS - Clear spacing */
    [data-testid="column"] {{
        padding: 0 !important;
    }}
    
    [data-testid="stHorizontalBlock"] {{
        gap: 16px !important;
        align-items: stretch !important;
    }}

    /* TABS - Clean style */
    [data-testid="stTabs"] [data-baseweb="tab-list"] {{
        background: transparent !important;
        padding: 0 !important;
        border-bottom: 2px solid var(--border) !important;
        margin-bottom: 24px !important;
        display: flex !important;
        gap: 32px !important;
    }}

    button[data-baseweb="tab"] {{
        background: transparent !important;
        color: var(--text-secondary) !important;
        border: none !important;
        border-bottom: 3px solid transparent !important;
        border-radius: 0 !important;
        margin: 0 !important;
        padding: 8px 0 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
    }}

    button[data-baseweb="tab"][aria-selected="true"] {{
        color: var(--accent) !important;
        border-bottom-color: var(--accent) !important;
        text-shadow: none !important;
    }}
    
    button[data-baseweb="tab"]:hover {{
        color: var(--text-primary) !important;
    }}


    /* ═══════════════════════════════════════════════════════
       BUTTON SYSTEM — 3-Tier: Primary | Ghost | Danger
    ═══════════════════════════════════════════════════════ */

    /* Base styles */
    .stButton button {{
        font-family: var(--font-heading) !important;
        font-weight: 800 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.8px !important;
        border-radius: 14px !important;
        padding: 0.7rem 1.4rem !important;
        transition: all 0.25s ease !important;
        cursor: pointer !important;
        position: relative !important;
        overflow: hidden !important;
        white-space: nowrap !important;
        border: none !important;
    }}

    /* Primary button */
    .stButton button[kind="primary"],
    .stButton button:not([kind="secondary"]) {{
        background: linear-gradient(135deg, {theme['accent']} 0%, {theme['accent_secondary']} 100%) !important;
        color: #fff !important;
        box-shadow: 
            0 4px 15px {theme['accent']}35,
            0 8px 30px {theme['accent']}25,
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }}
    
    .stButton button:not([kind="secondary"]):hover {{
        transform: scale(1.05) translateY(-4px) !important;
        box-shadow: 
            0 8px 25px {theme['accent']}45,
            0 16px 50px {theme['accent']}35,
            0 0 40px {theme['accent']}40,
            inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
        filter: brightness(1.12) !important;
    }}
    
    .stButton button:not([kind="secondary"]):active {{
        transform: scale(0.98) translateY(-2px) !important;
        box-shadow: 
            0 2px 8px {theme['accent']}30,
            inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
    }}

    /* Secondary button */
    .stButton button[kind="secondary"] {{
        background: linear-gradient(135deg, {theme['accent']}18, {theme['accent']}08) !important;
        color: {theme['accent']} !important;
        border: 2px solid {theme['accent']}50 !important;
        box-shadow: 
            0 2px 8px {theme['accent']}15,
            inset 0 1px 0 rgba(255, 255, 255, 0.5) !important;
        font-weight: 700 !important;
    }}
    
    .stButton button[kind="secondary"]:hover {{
        background: linear-gradient(135deg, {theme['accent']}28, {theme['accent']}18) !important;
        border-color: {theme['accent']} !important;
        transform: scale(1.04) translateY(-2px) !important;
        box-shadow: 
            0 6px 20px {theme['accent']}35,
            0 0 30px {theme['accent']}25,
            inset 0 1px 0 rgba(255, 255, 255, 0.6) !important;
        filter: brightness(1.08) !important;
    }}

    /* Error button */
    .error-btn .stButton button, .error-btn button {{
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(239, 68, 68, 0.08)) !important;
        color: #ef4444 !important;
        border: 2px solid rgba(239, 68, 68, 0.5) !important;
        box-shadow: 
            0 2px 8px rgba(239, 68, 68, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
        font-weight: 700 !important;
    }}
    
    .error-btn .stButton button:hover, .error-btn button:hover {{
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.25), rgba(239, 68, 68, 0.15)) !important;
        border-color: #ef4444 !important;
        transform: scale(1.04) translateY(-2px) !important;
        box-shadow: 
            0 4px 15px rgba(239, 68, 68, 0.35),
            0 8px 25px rgba(239, 68, 68, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
        filter: brightness(1.08) !important;
    }}

    /* Warning button */
    .warning-btn .stButton button {{
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(245, 158, 11, 0.08)) !important;
        color: #f59e0b !important;
        border: 2px solid rgba(245, 158, 11, 0.5) !important;
        box-shadow: 
            0 2px 8px rgba(245, 158, 11, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
        font-weight: 700 !important;
    }}
    
    .warning-btn .stButton button:hover {{
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.25), rgba(245, 158, 11, 0.15)) !important;
        border-color: #f59e0b !important;
        transform: scale(1.04) translateY(-2px) !important;
        box-shadow: 
            0 4px 15px rgba(245, 158, 11, 0.35),
            0 8px 25px rgba(245, 158, 11, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
        filter: brightness(1.08) !important;
    }}

    /* Success button */
    .success-btn .stButton button {{
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(16, 185, 129, 0.08)) !important;
        color: #10b981 !important;
        border: 2px solid rgba(16, 185, 129, 0.5) !important;
        box-shadow: 
            0 2px 8px rgba(16, 185, 129, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
        font-weight: 700 !important;
    }}
    
    .success-btn .stButton button:hover {{
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.25), rgba(16, 185, 129, 0.15)) !important;
        border-color: #10b981 !important;
        transform: scale(1.04) translateY(-2px) !important;
        box-shadow: 
            0 4px 15px rgba(16, 185, 129, 0.35),
            0 8px 25px rgba(16, 185, 129, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
        filter: brightness(1.08) !important;
    }}

    /* Download button */
    [data-testid="stDownloadButton"] button {{
        background: linear-gradient(135deg, rgba(100, 116, 139, 0.15), rgba(100, 116, 139, 0.08)) !important;
        color: #64748b !important;
        border: 2px solid rgba(100, 116, 139, 0.45) !important;
        border-radius: 12px !important;
        font-size: 0.82rem !important;
        padding: 0.5rem 1rem !important;
        font-weight: 700 !important;
        transition: all 0.2s ease !important;
        box-shadow: 
            0 2px 8px rgba(100, 116, 139, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
    }}
    
    [data-testid="stDownloadButton"] button:hover {{
        background: linear-gradient(135deg, rgba(100, 116, 139, 0.25), rgba(100, 116, 139, 0.15)) !important;
        border-color: #94a3b8 !important;
        transform: scale(1.03) translateY(-2px) !important;
        box-shadow: 
            0 4px 15px rgba(100, 116, 139, 0.3),
            0 8px 25px rgba(100, 116, 139, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
        filter: brightness(1.08) !important;
    }}

    /* Sidebar button */
    [data-testid="stSidebar"] .stButton button {{
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(239, 68, 68, 0.08)) !important;
        color: #ef4444 !important;
        border: 2px solid rgba(239, 68, 68, 0.45) !important;
        font-size: 0.82rem !important;
        padding: 0.45rem 1rem !important;
        border-radius: 50px !important;
        font-weight: 700 !important;
        box-shadow: 
            0 2px 8px rgba(239, 68, 68, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
    }}
    
    [data-testid="stSidebar"] .stButton button:hover {{
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.25), rgba(239, 68, 68, 0.15)) !important;
        border-color: #ef4444 !important;
        transform: scale(1.03) translateY(-1px) !important;
        box-shadow: 
            0 3px 12px rgba(239, 68, 68, 0.3),
            0 6px 20px rgba(239, 68, 68, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
        filter: brightness(1.08) !important;
    }}

    /* General Widget & Input fields - Ensure readability across themes */
    .stTextInput input, .stSelectbox [data-baseweb="select"], 
    .stFileUploader section[data-testid="stFileUploadDropzone"], .stMarkdown code {{
        background: var(--panel) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 0.95rem !important;
        color: var(--text-primary) !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
        margin: 0 !important;
    }}

    .stTextArea textarea {{
        background: rgba(255, 255, 255, 0.85) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 0.95rem !important;
        color: #1E293B !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
        margin: 0 !important;
    }}
    
    /* File Uploader Internal Text & Icons Fix */
    .stFileUploader small, .stFileUploader [data-testid="stMarkdownContainer"] p, .stFileUploader span,
    .stFileUploader div[data-testid="stUploaderIcon"] {{
        color: #1E293B !important;
        fill: #1E293B !important;
    }}
    
    /* Ensure widget labels are always visible */
    [data-testid="stWidgetLabel"] p {{
        color: #1E293B !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
    }}
    
    ::placeholder {{
        color: #475569 !important;
        opacity: 0.6 !important;
    }}

    .stTextInput input:focus {{
        background: #ffffff !important;
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px {theme['accent']}20 !important;
    }}

    .stTextArea textarea:focus {{
        background: #ffffff !important;
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px {theme['accent']}20 !important;
    }}

    /* DROPDOWNS */
    .stSelectbox [data-baseweb="select"] {{
        background: #ffffff !important;
        border-radius: 12px !important;
        border: 1.5px solid var(--border) !important;
        color: var(--text-primary) !important;
        transition: all 0.3s ease !important;
    }}
    
    .stSelectbox [data-baseweb="select"]:hover {{
        background: #f8fafc !important;
        border-color: var(--accent) !important;
    }}

    /* EXPANDERS - Transparent containers */
    [data-testid="stExpander"] {{
        background: transparent !important;
        border: none !important;
    }}
    
    [data-testid="stExpander"] > div:first-child {{
        background: var(--panel) !important;
        backdrop-filter: blur(var(--blur)) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        transition: all 0.3s ease !important;
        color: var(--text-primary) !important;
    }}
    
    [data-testid="stExpander"] > div:first-child:hover {{
        background: linear-gradient(135deg, #FFFFFF 0%, #F3F4F6 100%) !important;
        border-color: #E5E7EB !important;
    }}
    
    [data-testid="stExpander"] > div:last-child {{
        background: transparent !important;
        border: none !important;
    }}

    /* RADIO BUTTONS */
    div[data-testid="stRadio"] label div[role="radio"] > div {{
        background-color: var(--accent) !important;
    }}
    
    div[data-testid="stRadio"] label div[role="radio"][aria-checked="true"] {{
        border-color: var(--accent) !important;
    }}

    /* ═══════════════════════════════════════════════════
       CARDS & RESULTS
    ═══════════════════════════════════════════════════ */
    
    .result-card {{
        background: var(--panel) !important;
        border-radius: 20px !important;
        padding: 24px !important;
        border: 1px solid var(--border) !important;
        margin: 16px 0 !important;
        box-shadow: var(--card-shadow) !important;
        backdrop-filter: blur(var(--blur)) !important;
        -webkit-backdrop-filter: blur(var(--blur)) !important;
        transition: all 0.3s ease !important;
        color: var(--text-primary) !important;
    }}
    
    .result-card:hover {{
        border-color: var(--accent) !important;
        box-shadow: 
            0 12px 40px rgba(0, 0, 0, 0.12),
            0 4px 2px rgba(0, 0, 0, 0.04),
            inset 0 1px 1px rgba(255, 255, 255, 0.1) !important;
        transform: translateY(-4px) scale(1.005) !important;
    }}

    /* BADGES */
    .badge {{
        background: linear-gradient(135deg, {theme['accent']}30, {theme['accent']}15) !important;
        color: var(--accent) !important;
        padding: 6px 14px !important;
        border-radius: 20px !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        border: 1.5px solid {theme['accent']}50 !important;
        display: inline-block !important;
        box-shadow: 
            0 4px 12px {theme['accent']}20,
            inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
        backdrop-filter: blur(4px) !important;
    }}

    /* ═══════════════════════════════════════════════════
       CONVERSATION BUBBLES
    ═══════════════════════════════════════════════════ */
    
    .conv-container {{
        display: flex;
        flex-direction: column;
        gap: 16px;
        padding: 16px 0;
        max-height: 500px;
        overflow-y: auto;
        scroll-behavior: smooth;
    }}
    
    .bubble {{
        max-width: 80%;
        padding: 14px 16px;
        border-radius: 16px;
        font-size: 0.95rem;
        position: relative;
        line-height: 1.5;
        box-shadow: 
            0 4px 15px rgba(0, 0, 0, 0.12),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
        word-wrap: break-word;
        backdrop-filter: blur(8px) !important;
        transition: all 0.2s ease !important;
    }}
    
    .bubble-left {{
        align-self: flex-start;
        background: var(--panel) !important;
        color: var(--text-primary) !important;
        border: 1.5px solid var(--border) !important;
    }}
    
    .bubble-right {{
        align-self: flex-end;
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-secondary) 100%) !important;
        color: white !important;
        box-shadow: 
            0 6px 20px var(--accent)40,
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }}
    
    .bubble:hover {{
        transform: translateY(-2px) !important;
    }}
    
    .bubble-info {{
        font-size: 10px;
        opacity: 0.7;
        margin-bottom: 8px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    
    .bubble-trans {{
        margin-top: 8px;
        padding-top: 8px;
        border-top: 1px solid rgba(0,0,0,0.08);
        font-weight: 600;
        font-size: 0.9rem;
    }}
    
    .bubble-right .bubble-trans {{
        border-top: 1px solid rgba(255,255,255,0.2);
    }}
    .roll-container {{
        display: flex !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        padding: 5px 0 20px 0 !important;
        gap: 16px !important;
        scroll-snap-type: x mandatory !important;
        -webkit-overflow-scrolling: touch !important;
    }}
    .roll-container::-webkit-scrollbar {{
        height: 6px !important;
    }}
    .roll-container::-webkit-scrollbar-track {{
        background: rgba(0,0,0,0.05) !important;
        border-radius: 10px !important;
    }}
    .roll-container::-webkit-scrollbar-thumb {{
        background: var(--accent)50 !important;
        border-radius: 10px !important;
    }}
    .roll-item {{
        flex: 0 0 280px !important;
        scroll-snap-align: start !important;
        margin: 0 !important;
    }}

    /* DROPDOWNS & SELECTS - Modern White Cards */
    .stSelectbox [data-baseweb="select"], .stSelectbox div[role="button"] {{
        background: #ffffff !important;
        border: 1px solid rgba(59, 130, 246, 0.15) !important;
        border-radius: 14px !important;
        padding: 8px 12px !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.05) !important;
        color: #1E293B !important;
        font-weight: 600 !important;
    }}

    /* ═══════════════════════════════════════════════════
       RECENT DOCS CAROUSEL (SIDEBAR)
    ═══════════════════════════════════════════════════ */
    .recent-doc-card {{
        position: relative;
        background: var(--panel) !important;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 12px;
        border: 1.5px solid var(--border) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        align-items: center;
        gap: 12px;
        overflow: hidden;
    }}
    
    .recent-doc-card:hover {{
        transform: translateX(8px) scale(1.02);
        border-color: var(--accent) !important;
        box-shadow: 
            -4px 0 0 var(--accent),
            0 10px 25px rgba(0, 0, 0, 0.05);
    }}
    
    .doc-icon-box {{
        width: 36px;
        height: 36px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 10px;
        flex-shrink: 0;
    }}
    
    .doc-icon-pdf {{ background: #FEF2F2; color: #EF4444; }}
    .doc-icon-img {{ background: #F0FDF4; color: #10B981; }}
    
    .recent-doc-card .info {{
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }}
    
    .recent-doc-card .name {{
        font-size: 12px;
        font-weight: 700;
        color: var(--text-primary) !important;
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
    }}
    
    .recent-doc-card .meta {{
        font-size: 10px;
        display: flex;
        align-items: center;
        gap: 6px;
        margin-top: 2px;
    }}
    
    .lang-pill {{ background: var(--accent)15; color: var(--accent); padding: 2px 6px; border-radius: 4px; font-weight: 800; text-transform: uppercase; }}
    
    /* Translation Panels & Buttons */
    .translate-panel {{
        background: var(--panel) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 20px;
        padding: 28px 24px 20px 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.03);
    }}
    .cta-btn-wrap .stButton button {{
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-secondary) 100%) !important;
        color: white !important;
        font-size: 1.05rem !important;
        font-weight: 800 !important;
        padding: 0.85rem 1.6rem !important;
        border-radius: 16px !important;
        border: none !important;
        box-shadow: 0 6px 20px var(--glow) !important;
        transition: all 0.2s ease !important;
    }}
    .visual-btn-wrap .stButton button {{
        background: var(--bg) !important;
        color: var(--accent) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 14px !important;
    }}

    /* Learning & Activity Styles */
    .game-v2-card {{
        background: white !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 24px !important;
        padding: 24px !important;
        position: relative;
        box-shadow: 0 4px 20px rgba(0,0,0,0.02) !important;
        transition: all 0.3s ease !important;
        height: 100%; display: flex; flex-direction: column;
    }}
    .game-v2-card:hover {{ transform: translateY(-8px) !important; box-shadow: 0 20px 40px rgba(0,0,0,0.1) !important; }}
    .game-v2-icon-box {{ width: 64px; height: 64px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 32px; margin-bottom: 24px; transition: transform 0.3s ease; }}
    .game-v2-title {{ font-size: 20px; font-weight: 800; color: #1E293B !important; margin-bottom: 8px; letter-spacing: -0.5px; }}
    .game-v2-desc {{ font-size: 14px; color: #64748B !important; line-height: 1.5; margin-bottom: 24px; min-height: 42px; }}
    .flashcard {{ min-width: 200px; max-width: 200px; background: var(--panel); border: 1.5px solid var(--border); border-radius: 14px; padding: 16px; flex-shrink: 0; cursor: pointer; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03); transition: all 180ms ease; }}
    .flashcard:hover {{ border-color: var(--accent)50; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06); transform: translateY(-3px); }}

    /* Global Glowy Panel Style */
    .sidebar-card, .result-card {{
        background: var(--panel) !important;
        padding: 30px !important;
        border-radius: 24px !important;
        margin-bottom: 24px !important;
        border: 1px solid var(--border) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02) !important;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        animation: fadeInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) backwards;
    }}
    .sidebar-card:hover, .result-card:hover {{
        box-shadow: 0 20px 40px var(--glow) !important;
        transform: translateY(-8px) scale(1.02) !important;
        border-color: var(--accent) !important;
    }}

    /* ═══════════════════════════════════════════════════
       ALIGNMENT & SPACING IMPROVEMENTS
    ═══════════════════════════════════════════════════ */

    /* Columns - vertically align children to center */
    [data-testid="column"] {{
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        gap: 0 !important;
        padding: 0 8px !important;
    }}

    /* First column has no left padding */
    [data-testid="column"]:first-child {{
        padding-left: 0 !important;
    }}

    /* Last column has no right padding */
    [data-testid="column"]:last-child {{
        padding-right: 0 !important;
    }}

    /* Row containers — consistent vertical alignment */
    [data-testid="stHorizontalBlock"] {{
        align-items: flex-end !important;
        gap: 12px !important;
    }}

    /* All Streamlit buttons — uniform sizing and consistent look */
    .stButton {{
        display: flex !important;
        width: 100% !important;
    }}
    .stButton > button {{
        width: 100% !important;
        min-height: 46px !important;
        height: 46px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border-radius: 12px !important;
        font-size: 0.88rem !important;
        font-weight: 700 !important;
        padding: 0 1.2rem !important;
        letter-spacing: 0.3px !important;
        white-space: nowrap !important;
        box-sizing: border-box !important;
    }}

    /* Inputs and Selects — same height so they line up in rows */
    .stTextInput input,
    .stSelectbox [data-baseweb="select"] > div,
    .stSelectbox [data-baseweb="select"] {{
        min-height: 46px !important;
        height: 46px !important;
        box-sizing: border-box !important;
        border-radius: 12px !important;
        padding: 0 14px !important;
        font-size: 0.92rem !important;
        display: flex !important;
        align-items: center !important;
    }}

    /* TextArea — consistent padding */
    .stTextArea textarea {{
        border-radius: 14px !important;
        padding: 14px 16px !important;
        font-size: 0.93rem !important;
        line-height: 1.6 !important;
        resize: vertical !important;
    }}

    /* Widget labels — consistent spacing above inputs */
    [data-testid="stWidgetLabel"] {{
        margin-bottom: 4px !important;
        margin-top: 0 !important;
    }}
    [data-testid="stWidgetLabel"] p {{
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.4px !important;
        text-transform: uppercase !important;
        color: #64748B !important;
        margin: 0 0 4px 0 !important;
    }}

    /* Selectbox arrow and text vertical centering */
    .stSelectbox [data-baseweb="select"] [data-testid="stMarkdownContainer"],
    .stSelectbox [data-baseweb="select"] > div > div {{
        display: flex !important;
        align-items: center !important;
    }}

    /* File uploader — clean and consistent */
    .stFileUploader section, [data-testid="stFileUploadDropzone"] {{
        border-radius: 14px !important;
        padding: 16px 20px !important;
        min-height: 80px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
    }}

    /* Dividers — subtle */
    hr {{
        border: none !important;
        border-top: 1.5px solid rgba(59, 130, 246, 0.1) !important;
        margin: 20px 0 !important;
    }}

    /* Download button — match button height */
    [data-testid="stDownloadButton"] button {{
        min-height: 46px !important;
        height: 46px !important;
        border-radius: 12px !important;
        font-size: 0.88rem !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }}

    /* Checkbox alignment */
    [data-testid="stCheckbox"] {{
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
    }}

    /* Radio button alignment */
    [data-testid="stRadio"] > div {{
        display: flex !important;
        flex-direction: row !important;
        gap: 12px !important;
        flex-wrap: wrap !important;
    }}

    /* Tabs label padding and alignment */
    [data-testid="stTabs"] [data-baseweb="tab-list"] {{
        padding: 0 !important;
        gap: 8px !important;
        border-bottom: 2px solid rgba(59, 130, 246, 0.1) !important;
        margin-bottom: 20px !important;
    }}

    button[data-baseweb="tab"] {{
        padding: 10px 18px !important;
        border-radius: 10px 10px 0 0 !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
        min-width: fit-content !important;
    }}

    /* Expander header alignment */
    [data-testid="stExpander"] summary {{
        display: flex !important;
        align-items: center !important;
        padding: 12px 16px !important;
        min-height: 50px !important;
        font-weight: 600 !important;
        font-size: 0.93rem !important;
    }}

    /* st.columns gap standardization */
    [data-testid="stHorizontalBlock"] > div[data-testid="column"] {{
        box-sizing: border-box !important;
    }}

    /* Reduce excessive top/bottom spacers Streamlit generates */
    .element-container {{
        margin-bottom: 8px !important;
    }}

    /* Subheader and text spacing */
    h2 {{ margin-top: 24px !important; margin-bottom: 12px !important; }}
    h3 {{ margin-top: 16px !important; margin-bottom: 8px !important; }}

    /* Rich light-blue gradient background */
    .stApp {{
        background:
            radial-gradient(ellipse at 10% 20%, rgba(186, 230, 253, 0.55) 0%, transparent 55%),
            radial-gradient(ellipse at 90% 80%, rgba(147, 197, 253, 0.45) 0%, transparent 55%),
            radial-gradient(ellipse at 50% 50%, rgba(224, 242, 254, 0.6) 0%, transparent 70%),
            linear-gradient(160deg, #f0f9ff 0%, #e0f2fe 50%, #bfdbfe 100%) !important;
        background-attachment: fixed !important;
        color: #1E293B !important;
    }}

    /* All panels, cards, inputs — transparent glass, NO heavy white */
    .stTextInput input,
    .stSelectbox [data-baseweb="select"],
    .stTextArea textarea,
    [data-baseweb="popover"], [role="listbox"], [data-baseweb="menu"],
    [role="option"], [data-baseweb="menu"] li,
    [data-testid="stExpander"] > div:first-child,
    .result-card, .sidebar-card, .translate-panel, .game-v2-card, .flashcard {{
        background: rgba(255, 255, 255, 0.25) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        color: #1E293B !important;
        border: 1px solid rgba(186, 230, 253, 0.5) !important;
    }}

    /* Text areas — very light blue shade */
    .stTextArea textarea {{
        background: rgba(219, 234, 254, 0.35) !important;
        border: 1.5px solid rgba(147, 197, 253, 0.6) !important;
        color: #1E293B !important;
    }}
    .stTextArea textarea:focus {{
        background: rgba(219, 234, 254, 0.55) !important;
        border-color: rgba(59, 130, 246, 0.6) !important;
        box-shadow: 0 0 0 3px rgba(147, 197, 253, 0.2) !important;
    }}

    /* File uploader — transparent with blue dashed border */
    .stFileUploader section, [data-testid="stFileUploadDropzone"] {{
        background: rgba(255, 255, 255, 0.2) !important;
        border: 2px dashed rgba(59, 130, 246, 0.35) !important;
        color: #1E293B !important;
    }}

    /* Compact Dictionary Search Box */
    .dictionary-search-wrap .stTextInput input {{
        background: rgba(255, 255, 255, 0.3) !important;
        border: 1px solid rgba(186, 230, 253, 0.6) !important;
        border-radius: 12px !important;
        padding: 10px 16px !important;
        font-size: 0.95rem !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        color: #1E3A8A !important;
        height: 48px !important;
        box-shadow: none !important;
    }}

    .context-card {{
        background: rgba(255, 255, 255, 0.1) !important;
        border-radius: 14px !important;
        padding: 15px !important;
        margin-bottom: 12px !important;
        border: 1px solid rgba(186, 230, 253, 0.3) !important;
        transition: all 0.3s ease !important;
    }}

    .context-card:hover {{
        background: rgba(255, 255, 255, 0.2) !important;
        transform: translateY(-2px);
    }}

    /* Unified Search Bar styling */
    .unified-search-box {{
        display: flex !important;
        align-items: stretch !important;
        background: rgba(255, 255, 255, 0.2) !important;
        border-radius: 16px !important;
        border: 1.5px solid rgba(186, 230, 253, 0.5) !important;
        overflow: hidden !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03) !important;
        margin-bottom: 30px !important;
    }}

    .unified-search-box [data-testid="column"] {{
        padding: 0 !important;
    }}
    
    .unified-search-box [data-testid="stHorizontalBlock"] {{
        gap: 0 !important;
    }}

    .unified-search-box .stTextInput {{
        flex: 1 !important;
        margin-bottom: 0 !important;
    }}

    .unified-search-box .stTextInput input {{
        background: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        height: 52px !important;
        padding-left: 20px !important;
    }}

    .unified-search-box .stButton {{
        width: auto !important;
    }}

    .unified-search-box .stButton button {{
        border-radius: 0 !important;
        height: 52px !important;
        border: none !important;
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-secondary) 100%) !important;
        padding: 0 25px !important;
        font-weight: 800 !important;
        color: white !important;
        margin: 0 !important;
    }}

    .unified-search-box:focus-within {{
        border-color: var(--accent) !important;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.15) !important;
        background: rgba(255, 255, 255, 0.3) !important;
    }}

    .dictionary-search-wrap .stTextInput input:focus {{
        border-color: var(--accent) !important;
        background: rgba(255, 255, 255, 0.4) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2) !important;
    }}

    .dictionary-search-wrap {{
        margin: 0 !important;
        padding: 0 !important;
    }}

    .dict-meaning-card {{
        background: rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(10px) !important;
        border-left: 4px solid var(--accent) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        margin-bottom: 20px !important;
        border: 1px solid rgba(186, 230, 253, 0.5);
        border-left-width: 4px !important;
        transition: transform 0.3s ease !important;
    }}

    .dict-meaning-card:hover {{
        transform: translateX(10px) !important;
        background: rgba(255, 255, 255, 0.3) !important;
    }}
</style>

"""
