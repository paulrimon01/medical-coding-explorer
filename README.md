# medical-coding-explorer
Interactive visualization tool for the paper "Interpretable Dynamic Rule Attention for Medical Coding." compares the attention focus of a standard BioClinicalBERT against our Rule-Guided model on MIMIC-III discharge summaries.

# 🏥 Medical Coding Attention Explorer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

This repository hosts the interactive visualization tool for the paper **"Interpretable Dynamic Rule Attention for Medical Coding"** (Canadian AI 2026).

It allows researchers and clinicians to visualize and compare how different neural network models process clinical text when predicting ICD-9 diagnosis codes.

## 🔍 What does this tool do?
Neural networks like BERT are often "black boxes." This tool opens the box by visualizing the **Attention Weights**—showing exactly which words the model focused on when making a decision.

You can compare two models side-by-side:
1.  **🤖 Baseline Model (BioClinicalBERT):** A standard pretrained medical BERT model.
2.  **🩺 Rule-Guided Model (Ours):** A modified architecture that injects domain knowledge (ICD-9 keyword rules) directly into the attention mechanism.

## 🚀 Live Demo
You can view the live application here:
**[Insert Your Streamlit App URL Here]**

*(Note: If the link is not active, follow the "Local Installation" steps below)*

## 📂 Project Structure
* `app.py`: The main Streamlit application code.
* `model_viz_data.json`: Pre-computed attention weights and tokens extracted from the MIMIC-III test set (50 sampled patients).
* `requirements.txt`: Python dependencies required to run the app.

## 💻 Local Installation
If you prefer to run this on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR-USERNAME/medical-coding-explorer.git](https://github.com/YOUR-USERNAME/medical-coding-explorer.git)
    cd medical-coding-explorer
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

## 📊 How to Interpret the Visuals
* **Opacity:** The darkness of the background color represents the **Attention Weight**.
    * **Darker Color** = The model paid high attention to this word.
    * **Lighter Color** = The model ignored this word.
* **Baseline (Blue):** Often shows "diffuse" attention, focusing on separators, punctuation, or generic medical terms.
* **Rule-Guided (Purple):** Designed to "spike" attention on clinically diagnostic terms (e.g., *pneumonia*, *diabetes*, *sepsis*), improving interpretability for medical auditors.

## 📄 Citation
If you use this code or visualization in your research, please cite:

> [Author Name(s)], "Interpretable Dynamic Rule Attention for Medical Coding," *37th Canadian Conference on Artificial Intelligence (Canadian AI)*, 2026.

---
*Built with [Streamlit](https://streamlit.io) and [PyTorch](https://pytorch.org).*
