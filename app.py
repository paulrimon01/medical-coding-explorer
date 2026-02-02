import streamlit as st
import json

# --- Page Configuration ---
st.set_page_config(
    page_title="Medical Coding Interpretability",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Styles ---
st.markdown("""
    <style>
    .highlight-box {
        line-height: 1.6;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        background-color: #f9f9f9;
        font-family: sans-serif;
    }
    .token-span {
        padding: 0 3px;
        border-radius: 4px;
        margin: 0 1px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# --- Helper Function: Highlight Text ---
def highlight_text(tokens, weights, color_base):
    """
    Generates HTML to display tokens with background opacity proportional to attention weight.
    color_base: "blue" (baseline) or "purple" (rule-guided)
    """
    html_code = "<div class='highlight-box'>"
    
    # Define colors
    if color_base == "blue":
        # Base: #3498db (Blue)
        r, g, b = 52, 152, 219
    else:
        # Base: #9b59b6 (Purple)
        r, g, b = 155, 89, 182

    for token, weight in zip(tokens, weights):
        # Clean up tokens
        if token in ["[PAD]", "[CLS]", "[SEP]"]:
            continue
        
        # Visual trick: Square the weight to make high attention pop more
        # (Low weights become very transparent)
        opacity = weight ** 2 
        
        # Text color: White if background is dark, Black if light
        text_color = "white" if opacity > 0.6 else "black"
        
        html_code += f"<span class='token-span' style='background-color: rgba({r},{g},{b},{opacity}); color: {text_color};'>{token}</span> "
        
    html_code += "</div>"
    return html_code

# --- Load Data ---
@st.cache_data
def load_data():
    try:
        with open('model_viz_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

data = load_data()

# --- SIDEBAR ---
st.sidebar.title("🔍 Patient Explorer")
st.sidebar.info("Select a patient ID to compare how the Baseline (Standard BERT) and Rule-Guided models view the clinical text.")

if data:
    patient_id = st.sidebar.selectbox("Select Patient Record ID", [d['id'] for d in data])
    # Filter data for selected patient
    patient = next(p for p in data if p['id'] == patient_id)
else:
    st.error("Data file 'model_viz_data.json' not found. Please upload it to the repository.")
    st.stop()

# --- MAIN CONTENT ---
st.title("Interpretable Dynamic Rule Attention")
st.markdown("### Visualizing Model Focus for Medical Coding")
st.markdown("""
This tool visualizes the **Attention Mechanism** of two models processing the same discharge summary.
* **Opacity** represents attention strength (Darker = Higher Focus).
* **Goal:** The model should focus on clinically relevant terms (e.g., *'pneumonia'*, *'diabetes'*).
""")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🤖 Baseline BioClinicalBERT")
    st.caption("Standard Self-Attention (Often diffuse or focuses on punctuation)")
    html_base = highlight_text(patient['tokens'], patient['baseline_attention'], "blue")
    st.markdown(html_base, unsafe_allow_html=True)

with col2:
    st.subheader("🩺 Rule-Guided Attention (Ours)")
    st.caption("Dynamic Rule-Injected Attention (Focuses on diagnostic keywords)")
    html_rule = highlight_text(patient['tokens'], patient['rule_attention'], "purple")
    st.markdown(html_rule, unsafe_allow_html=True)

st.divider()
