import streamlit as st
import re
from llm_bias_classifier import analyze_plot_bias
from rewrite_plot_without_bias import rewrite_plot_without_bias
from visualization import draw_bias_bar_chart
# from generate_report import export_to_pdf  # Enable this only if WeasyPrint is working

st.set_page_config(page_title="Bollywood Gender Bias Analyzer", layout="wide")
st.title("🎬 Bollywood Plot Bias Analyzer (LLM-Powered)")

plot = st.text_area("📜 Paste any Bollywood movie plot here:", height=300, placeholder="Enter the plot...")

if st.button("🔍 Analyze Bias"):
    if not plot.strip():
        st.warning("⚠️ Please enter a movie plot before clicking Analyze.")
    else:
        with st.spinner("🧠 Running LLM bias detection and analysis..."):
            # STEP 1: Analyze Bias
            analysis = analyze_plot_bias(plot)

            st.subheader("🔎 Bias Analysis Report")
            st.text_area("📄 Sentence-Level Bias Classification", analysis, height=400)

            # STEP 2: Extract tags — handle multi-word category names
            bias_tags = re.findall(r"Type:\s*([^\n:]+)", analysis)

            # STEP 3: Visualize chart
            if bias_tags:
                st.subheader("📊 Bias Category Distribution")
                draw_bias_bar_chart(bias_tags)
                st.image("bias_distribution.png")
            else:
                st.warning("⚠️ No bias tags detected — skipping chart generation.")

            # STEP 4: Rewrite without bias
            st.subheader("📝 Rewritten Bias-Free Plot")
            new_plot = rewrite_plot_without_bias(plot)
            st.text_area("✍️ Rephrased Plot (Bias Removed)", new_plot, height=300)

            # STEP 5: (Optional) Export report
            summary_md = f"""
# Gender Bias Report

## 🎞️ Original Plot
{plot}

## 🔍 Bias Analysis
{analysis}

## 📝 Rewritten Plot
{new_plot}
"""
            # Uncomment if WeasyPrint is installed and configured:
            # export_to_pdf(summary_md)
            # st.success("📄 Report saved as 'bias_report.pdf'")
