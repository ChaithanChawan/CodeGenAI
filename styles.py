"""CSS styling for the dark-purple Streamlit interface."""

import streamlit as st

def apply_styles():
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: #0b0b12;
            color: #f4f2fa;
        }
        [data-testid="stHeader"] {
            background: rgba(11, 11, 18, 0.9);
        }
        [data-testid="stSidebar"] {
            background: #11101b;
            border-right: 1px solid #29243b;
        }
        .block-container {
            max-width: 1500px;
            padding-top: 1.8rem;
            padding-bottom: 3rem;
        }
        .hero {
            background: linear-gradient(135deg, #19132b, #11101b 75%);
            border: 1px solid #39275c;
            border-radius: 20px;
            padding: 28px;
            margin-bottom: 22px;
        }
        .eyebrow {
            color: #bb9aff;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        .hero h1 {
            color: #ffffff;
            font-size: 2.35rem;
            margin: 8px 0;
        }
        .hero p {
            color: #b9b4ca;
            font-size: 1rem;
            margin-bottom: 0;
        }
        .section-heading {
            color: #eee9fa;
            font-size: 1.15rem;
            font-weight: 650;
            margin-bottom: 8px;
        }
        .panel {
            background: #12111c;
            border: 1px solid #2b273b;
            border-radius: 16px;
            padding: 20px;
        }
        .muted {
            color: #a8a2b9;
            font-size: 0.88rem;
        }
        [data-testid="stTextArea"] textarea {
            background: #100f19;
            border: 1px solid #39324e;
            border-radius: 12px;
            color: #f6f3ff;
            line-height: 1.6;
        }
        [data-testid="stTextArea"] textarea:focus {
            border-color: #a78bfa;
            box-shadow: 0 0 0 1px #a78bfa;
        }
        .stButton > button {
            border-radius: 10px;
            border: 1px solid #39324e;
            transition: all 0.15s ease;
        }
        .stButton > button[kind="primary"] {
            background: linear-gradient(100deg, #7c3aed, #9b5cf6);
            border: 1px solid #a78bfa;
            color: white;
            font-weight: 650;
        }
        .stButton > button:hover {
            border-color: #a78bfa;
            color: white;
        }
        [data-testid="stCode"] {
            border: 1px solid #302a43;
            border-radius: 12px;
        }
        [data-testid="stMetric"] {
            background: #151321;
            border: 1px solid #302a43;
            padding: 12px;
            border-radius: 12px;
        }
        hr {
            border-color: #29243b;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
