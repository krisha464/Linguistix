import streamlit as st

def render_fun_zone(render_word_games):
    st.markdown("""
    <style>
        @keyframes bounce-slow {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .game-v2-card {
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            animation: bounce-slow 4s ease-in-out infinite;
        }
        .game-v2-card:hover {
            transform: scale(1.05) rotate(1deg) !important;
            box-shadow: 0 25px 50px rgba(0,0,0,0.1) !important;
        }
        .sticker {
            position: absolute;
            font-size: 40px;
            opacity: 0.15;
            bottom: -10px;
            right: -10px;
            transform: rotate(-15deg);
        }
    </style>
    """, unsafe_allow_html=True)

    # === FUN ACTIVITY HUB ONLY ===
    st.markdown("""
        <div style='text-align:center; margin: 20px 0 40px 0;'>
            <h2 style="font-size:42px; font-weight:900; color:var(--text-primary); letter-spacing: -1.5px; margin:0;">🧩 Game Zone <span style='font-size:30px;'>✨</span></h2>
            <p style="font-size:16px; color:var(--text-secondary); margin-top:4px; font-weight:600;">Pick a challenge and start playing! 🌈</p>
        </div>
    """, unsafe_allow_html=True)

    # 3-Column Activity Grid
    r1_c1, r1_c2, r1_c3 = st.columns(3, gap="large")
    
    with r1_c1:
        st.markdown("""
        <div class="game-v2-card" style="border-top: 6px solid #3B82F6; background:var(--panel);">
            <div class="game-v2-badge recommended-badge">🔥 HOT</div>
            <div class="game-v2-icon-box" style="background:#EFF6FF; color:#3B82F6;">🧠</div>
            <div class="game-v2-title">Word Quest</div>
            <div class="game-v2-desc">A fun daily quiz to find new words!</div>
            <div class="game-v2-stat">⭐ 100+ Played</div>
            <div class="sticker">🎯</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Start Quest", key="game_fun_quiz", use_container_width=True):
            st.session_state.word_games_selected = 'quiz'
            render_word_games()

    with r1_c2:
        st.markdown("""
        <div class="game-v2-card" style="border-top: 6px solid #F59E0B; background:var(--panel); animation-delay: 0.5s;">
            <div class="game-v2-badge" style="background:#FFFBEB; color:#F59E0B;">PUZZLE</div>
            <div class="game-v2-icon-box" style="background:#FFFBEB; color:#78350F;">🔍</div>
            <div class="game-v2-title">Pair Finder</div>
            <div class="game-v2-desc">Find matching word cards together!</div>
            <div class="game-v2-stat">🧩 Skill Level: Fun</div>
            <div class="sticker">🍭</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔍 Find Pairs", key="game_fun_syn", use_container_width=True):
            st.session_state.word_games_selected = 'syn_ant'
            render_word_games()

    with r1_c3:
        st.markdown("""
        <div class="game-v2-card" style="border-top: 6px solid #10B981; background:var(--panel); animation-delay: 1s;">
            <div class="game-v2-badge" style="background:#ECFDF5; color:#10B981;">NEW</div>
            <div class="game-v2-icon-box" style="background:#ECFDF5; color:#065F46;">🌐</div>
            <div class="game-v2-title">Word Detective</div>
            <div class="game-v2-desc">Guess which language is hidden!</div>
            <div class="game-v2-stat">🕵️ Detective Rank</div>
            <div class="sticker">💎</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🕵️ Solve Case", key="game_fun_detect", use_container_width=True):
            st.session_state.word_games_selected = 'lang_detect'
            render_word_games()

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)
    
    # Row 2
    r2_c1, r2_c2, r2_c3 = st.columns(3, gap="large")

    with r2_c1:
        st.markdown("""
        <div class="game-v2-card" style="border-top: 6px solid #8B5CF6; background:var(--panel); animation-delay: 1.5s;">
            <div class="game-v2-icon-box" style="background:#F5F3FF; color:#5B21B6;">📚</div>
            <div class="game-v2-title">Story Master</div>
            <div class="game-v2-desc">Learn how to use words in stories</div>
            <div class="game-v2-stat">✨ Creative Mode</div>
            <div class="sticker">📖</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📖 Read Story", key="game_fun_context", use_container_width=True):
            st.session_state.word_games_selected = 'context_master'
            render_word_games()

    with r2_c2:
        st.markdown("""
        <div class="game-v2-card" style="border-top: 6px solid #F97316; background:var(--panel); animation-delay: 2s;">
            <div class="game-v2-badge" style="background:#FFF7ED; color:#F97316;">ACTION</div>
            <div class="game-v2-icon-box" style="background:#FFF7ED; color:#9A3412;">⚡</div>
            <div class="game-v2-title">Lightning Blitz</div>
            <div class="game-v2-desc">Match the words as fast as you can!</div>
            <div class="game-v2-stat">🏆 Speed Star</div>
            <div class="sticker">⚡</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("⚡ Start Blitz", key="game_fun_speed", use_container_width=True):
            st.session_state.word_games_selected = 'speed_trans'
            render_word_games()

    with r2_c3:
        st.markdown("""
        <div class="game-v2-card" style="background: var(--panel) !important; border: 2px dashed var(--border) !important; opacity:0.6;">
            <div class="game-v2-badge" style="background:var(--border); color:var(--text-secondary);">SOON</div>
            <div class="game-v2-icon-box" style="background:white; border: 1px solid var(--border); color:#94A3B8;">🎁</div>
            <div class="game-v2-title">Secret Level</div>
            <div class="game-v2-desc">A mystery activity is coming soon!</div>
            <div class="game-v2-stat">🔒 Locked</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Mystery Box", key="game_fun_mystery", use_container_width=True, disabled=True)
