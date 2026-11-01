import streamlit as st

from config import APP_TITLE, MODEL, EXAMPLES
from styles import apply_styles
from generator import stream_gemini_response
from utils import extract_code_and_explanation, check_python_syntax

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded",
)

def render_result(container, result):
    """Display generated code, syntax status, download, and metrics."""
    with container.container():
        st.markdown("#### ✨ Python solution")
        if result.get("syntax_ok", False):
            st.success(result.get("syntax_message", "Syntax check passed."))
        else:
            st.error(result.get("syntax_message", "Syntax needs review."))

        st.code(result["code"], language="python")
        st.download_button(
            "⬇️ Download .py file",
            data=result["code"],
            file_name="generated_code.py",
            mime="text/x-python",
            key=f"download_{id(result)}",
            use_container_width=True,
        )

        st.divider()
        st.markdown("#### Explanation")
        st.write(result.get("explanation", "No explanation provided."))

        metric1, metric2 = st.columns(2)
        with metric1:
            st.metric("Generation time", f"{result.get('elapsed', 0):.2f}s")
        with metric2:
            st.metric(
                "Syntax",
                "Passed" if result.get("syntax_ok") else "Needs review",
            )

        st.caption(
            "Syntax validation checks Python grammar only. It does not "
            "guarantee logical correctness or safety. Review generated code."
        )


# ---------- Session state ----------
st.session_state.setdefault("requirement", "")
st.session_state.setdefault("history", [])
st.session_state.setdefault("last_result", None)

def load_requirement(example):
    """Callback: set the text area value before Streamlit recreates it."""
    st.session_state.requirement = example

def restore_result(item):
    """Callback: restore a previous result and its requirement."""
    st.session_state.last_result = item
    st.session_state.requirement = item["requirement"]

def clear_history():
    st.session_state.history = []

apply_styles()

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## 💜 CodeGen AI")
    st.caption("AI-powered development workspace")
    st.divider()

    st.markdown("### Workspace")
    category = st.selectbox("Task category", list(EXAMPLES.keys()))
    st.button(
        "＋ Load example",
        use_container_width=True,
        on_click=load_requirement,
        args=(EXAMPLES[category],),
    )

    st.divider()
    st.markdown("### Capabilities")
    st.markdown(
        "🧠 Natural-language code generation\n\n"
        "⚡ Streaming AI responses\n\n"
        "✓ Python syntax validation\n\n"
        "↓ Download generated code\n\n"
        "◷ Recent generation history"
    )

    st.divider()
    st.markdown("### Model")
    st.code(MODEL, language="text")
    st.caption("Powered by the Gemini API")

    st.divider()
    st.markdown("### Recent generations")
    if not st.session_state.history:
        st.caption("Your recent generations will appear here.")
    else:
        for index, item in enumerate(st.session_state.history[:5]):
            label = item["requirement"].replace("\n", " ").strip()
            label = label[:48] + ("..." if len(label) > 48 else "")
            st.button(
                label or f"Generation {index + 1}",
                key=f"history_{index}",
                use_container_width=True,
                on_click=restore_result,
                args=(item,),
            )
        st.button(
            "Clear history",
            use_container_width=True,
            on_click=clear_history,
        )

# ---------- Header ----------
st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">YOUR AI CODING WORKSPACE</div>
        <h1>Build faster with AI. ✨</h1>
        <p>
            Transform natural-language requirements into readable Python
            code, with syntax validation and downloadable output.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="muted">WORKSPACE &nbsp; / &nbsp; PYTHON GENERATOR</div>',
    unsafe_allow_html=True,
)
st.write("")

# ---------- Split-screen workspace ----------
left, right = st.columns([1, 1.15], gap="large")

with left:
    st.markdown(
        '<div class="section-heading">01 &nbsp; Define your requirement</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="muted">Describe what your code should do.</div>',
        unsafe_allow_html=True,
    )

    requirement_text = st.text_area(
        "Software requirement",
        key="requirement",
        height=235,
        placeholder=(
            "Example:\n\nCreate a Python function that checks whether "
            "a number is prime. Handle edge cases and include a usage example."
        ),
        label_visibility="collapsed",
    )
    st.caption(
        "Tip: Include expected inputs, outputs, and edge cases for better results."
    )

    generate_clicked = st.button(
        "✦  Generate Python code",
        type="primary",
        use_container_width=True,
    )

    with st.expander("Explore example requirements"):
        for name, example in EXAMPLES.items():
            st.button(
                name,
                key=f"example_{name}",
                use_container_width=True,
                on_click=load_requirement,
                args=(example,),
            )

    st.markdown(
        '<div class="muted">Your API key stays in your local environment file.</div>',
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        '<div class="section-heading">02 &nbsp; Generated solution</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="muted">Your code and validation results appear here.</div>',
        unsafe_allow_html=True,
    )
    output_slot = st.empty()

# ---------- Generate code ----------
if generate_clicked:
    requirement = requirement_text.strip()
    if not requirement:
        with output_slot.container():
            st.warning("Enter a requirement before generating code.")
    else:
        chunks = []

        try:
            with output_slot.container():
                live_output = st.empty()
                live_output.markdown("#### ⏳ Connecting to Gemini...")

                answer, elapsed = stream_gemini_response(
                    requirement,
                    on_chunk=lambda current_text: live_output.markdown(
                        "#### ⚡ Generating...\n\n" + current_text
                    ),
                )

            if not answer.strip():
                with output_slot.container():
                    st.error("Gemini returned an empty response. Please try again.")
            else:
                code, explanation = extract_code_and_explanation(answer)
                syntax_ok, syntax_message = check_python_syntax(code)

                result = {
                    "requirement": requirement,
                    "code": code,
                    "explanation": explanation,
                    "elapsed": elapsed,
                    "syntax_ok": syntax_ok,
                    "syntax_message": syntax_message,
                }
                st.session_state.last_result = result
                st.session_state.history.insert(0, result)
                st.session_state.history = st.session_state.history[:10]

                render_result(output_slot, result)

        except Exception as error:
            with output_slot.container():
                st.error(
                    "Code generation failed. Check your internet connection, "
                    "Gemini API access, model availability, and API quota."
                )
                st.caption(f"{type(error).__name__}: {error}")

elif st.session_state.last_result:
    render_result(output_slot, st.session_state.last_result)
else:
    with output_slot.container():
        st.markdown(
            """
            <div class="panel">
                <h3>✨ Ready to generate</h3>
                <p class="muted">
                    Enter a requirement on the left and click Generate Python
                    code. Your solution will appear here.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------- Footer ----------
st.divider()
st.markdown(
    """
    <div style="text-align:center; color:#8e879f; padding:10px;">
        💜 CodeGen AI &nbsp; · &nbsp; TCS Hackathon Prototype
        <br>
        <span style="font-size:0.8rem;">
            Built with Python, Streamlit, and Gemini
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)
