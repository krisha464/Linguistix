import streamlit as st
import datetime
from utils.translator import detect_and_translate, SUPPORTED_LANGS
from utils.storage import save_data
from utils.doc_logic import extract_text_from_doc
from utils.speech import text_to_speech

def render_doc_translate(target_options, create_pdf):
    if not st.session_state.authenticated:
        st.markdown("""
        <div class="result-card" style="text-align:center; padding: 40px 20px;">
            <h2 style="color:var(--accent) !important; margin-bottom:10px;"><i class="fas fa-crown"></i> Go Pro</h2>
            <p style="font-size:1.1rem; opacity:0.9;">Professional translation tools for documents are reserved for members.</p>
            <div style="margin: 25px 0; text-align:left; display:inline-block; border-left: 2px solid var(--border); padding-left: 20px;">
                <p style="margin-bottom:8px;"><i class="fas fa-check-circle" style="color:var(--state-success);"></i> <b>Full Doc Import</b> - Translate Word &amp; PDFs instantly</p>
                <p style="margin-bottom:8px;"><i class="fas fa-check-circle" style="color:var(--state-success);"></i> <b>Batch Processing</b> - Translate entire CSV/JSON files</p>
                <p style="margin-bottom:8px;"><i class="fas fa-check-circle" style="color:var(--state-success);"></i> <b>Format Retention</b> - Keep your layouts intact</p>
            </div>
            <p style="font-weight:600; color:var(--text-secondary) !important;">Use the button in the top-right corner to unlock!</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Unlock Document Mode", width='stretch', key='unlock_doc_btn'):
            st.session_state.page = "auth"
            st.rerun()
    else:
        # Document translation UI for authenticated users
        st.markdown("<p style='font-size:0.9rem; opacity:0.7; margin-top:-8px;'>Upload a PDF, Word document, or text file to extract and translate its content instantly.</p>", unsafe_allow_html=True)

        st.markdown('<div class="translate-panel">', unsafe_allow_html=True)

        doc_target_options = [l for l in SUPPORTED_LANGS.keys() if l != "auto"]
        uploaded_doc = st.file_uploader(
            "📂 Upload a document (PDF, DOCX, or TXT)",
            type=["pdf", "docx", "txt"],
            key="doc_uploader"
        )

        if uploaded_doc:
            st.markdown(f"""
            <div style="background:var(--panel); border:1.5px solid var(--border); border-radius:12px;
                        padding:12px 16px; margin:8px 0 16px 0; display:flex; align-items:center; gap:10px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                <span style="font-size:1.4rem;">📄</span>
                <div style="overflow:hidden;">
                    <div style="font-weight:700; color:var(--text-primary); font-size:0.95rem; white-space:nowrap; text-overflow:ellipsis; overflow:hidden;">{uploaded_doc.name}</div>
                    <div style="font-size:0.78rem; color:var(--text-secondary); opacity:0.7;">{round(uploaded_doc.size/1024, 1)} KB &bull; {uploaded_doc.type.split('/')[-1].upper()}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            ctrl_row = st.columns([3, 2])
            with ctrl_row[0]:
                doc_tgt = st.selectbox(
                    "Translate to",
                    options=doc_target_options,
                    format_func=lambda x: SUPPORTED_LANGS[x],
                    key="doc_tgt_lang"
                )
            with ctrl_row[1]:
                st.markdown('<p style="font-size:0.875rem; font-weight:600; margin-bottom:4px; color:var(--text-primary); visibility:hidden;">_</p>', unsafe_allow_html=True)
                st.markdown('<div class="cta-btn-wrap">', unsafe_allow_html=True)
                doc_clicked = st.button("🚀 Translate Document", key="doc_translate_btn", type="primary", width='stretch')
                st.markdown('</div>', unsafe_allow_html=True)

            if doc_clicked:
                with st.spinner("📖 Extracting and translating..."):
                    file_bytes = uploaded_doc.read()
                    raw_text = extract_text_from_doc(file_bytes, uploaded_doc.type)
                    if raw_text.startswith("ERROR:"):
                        st.error(raw_text)
                    elif not raw_text.strip():
                        st.warning("No text could be extracted from this document.")
                    else:
                        translated, detected = detect_and_translate(raw_text, doc_tgt, "auto")
                        st.session_state.doc_result = translated
                        st.session_state.doc_detected = detected
                        st.session_state.doc_raw_text = raw_text
                        st.session_state.history.append({
                            "input": raw_text[:80],
                            "output": translated[:80],
                            "src": detected or "auto",
                            "tgt": doc_tgt,
                            "Time": datetime.datetime.now().strftime("%H:%M:%S"),
                            "filename": uploaded_doc.name,
                            "type": "doc"
                        })
                        save_data(st.session_state.history, st.session_state.favorites, st.session_state.phrasebook, username=st.session_state.username)
                        st.rerun()
        else:
            doc_tgt = doc_target_options[0] if doc_target_options else "es"

        st.markdown('</div>', unsafe_allow_html=True)

        # Show persisted doc result
        if st.session_state.doc_result:
            translation = st.session_state.doc_result
            detected = st.session_state.doc_detected
            raw_text = st.session_state.doc_raw_text or ""
            doc_tgt_disp = st.session_state.get('doc_tgt_lang', 'es')

            st.markdown(f"""
            <div class="result-card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                    <h3 style="margin:0; color:var(--accent) !important;">Document Translation</h3>
                    <span class="badge">📄 {detected.upper() if detected else 'AUTO'} → {doc_tgt_disp.upper()}</span>
                </div>
                <div style="background:var(--bg); border:1px solid var(--border); border-radius:12px; padding:12px 16px; margin-bottom:15px;">
                    <p style="font-size:11px; font-weight:800; color:var(--text-secondary); opacity:0.6; margin-bottom:4px; text-transform:uppercase;">Extracted Preview</p>
                    <p style="font-size:13px; color:var(--text-primary); font-style:italic;">{raw_text[:300]}...</p>
                </div>
                <hr style="opacity:0.1; margin: 15px 0;">
                <p style="font-size:11px; font-weight:800; color:var(--accent); text-transform:uppercase; margin-bottom:8px;">Translated Result</p>
                <p style="font-size: 1.05rem; line-height: 1.7; white-space: pre-wrap; font-weight:500;">{translation[:5000]}</p>
            </div>
            """, unsafe_allow_html=True)

            act_doc = st.columns(4)
            with act_doc[0]:
                if st.button("🔊 Listen", key="doc_listen", width='stretch'):
                    audio_bytes = text_to_speech(translation[:500], doc_tgt)
                    if audio_bytes:
                        st.session_state.audio_to_play = audio_bytes
                        st.rerun()
            with act_doc[1]:
                if st.button("⭐ Star", key="doc_star", width='stretch'):
                    st.session_state.favorites.append({"input": f"Doc: {raw_text[:40]}...", "output": translation[:80]})
                    save_data(st.session_state.history, st.session_state.favorites, st.session_state.phrasebook, username=st.session_state.username)
                    st.toast("Saved to favorites!")
            with act_doc[2]:
                pdf_data = create_pdf(translation)
                st.download_button("📄 PDF", data=pdf_data, file_name="doc_translation.pdf", width='stretch')
            with act_doc[3]:
                st.download_button("📝 TXT", data=translation, file_name="doc_translation.txt", mime="text/plain", width='stretch')

            if st.button("🗑️ Clear Result", key="doc_clear"):
                st.session_state.doc_result = None
                st.session_state.doc_raw_text = None
                st.session_state.doc_detected = None
                st.rerun()
        else:
            # Document result placeholder
            st.markdown("""
            <div style='background:var(--panel); border:1.5px dashed var(--border); border-radius:20px; padding:60px 20px; text-align:center; color:var(--text-secondary);'>
                <h3 style='color:var(--text-primary) !important; margin-bottom:10px;'>Translation Result</h3>
                <p style='font-size:14px; opacity:0.8;'>Upload and translate a document to see results here.</p>
            </div>
            """, unsafe_allow_html=True)
