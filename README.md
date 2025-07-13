# 🎬 Bollywood Gender Bias Analyzer (LLM-Powered)

An intelligent Streamlit-based web app that detects **gender bias** in Bollywood movie plots, visualizes the bias patterns, and suggests **rewritten unbiased versions** — all powered by **LLMs from Hugging Face**.




## 🔍 What It Does

- ✅ Takes any Bollywood movie plot as input
- 🤖 Uses a **local version** of DeepSeek’s `flan-t5-base` model to **detect gender bias** across more than 20+ stereotype categories
- 📊 Provides **visual charts** of detected bias types
- ✍️ Generates a **rewritten version** of the plot with reduced or removed gender stereotypes
- 📄 (Optional) Generates a downloadable PDF bias report




## 🧠 Model Used

We use **[`deepseek-ai/flan-t5-base`](https://huggingface.co/deepseek-ai/flan-t5-base)** — a lightweight but powerful open-source large language model that works entirely **offline** via local inference.

> Note: The actual model weights are not included in this repo due to size (1GB+). You'll need to manually download them into the folder described below.



## 📁 Project Structure

new_try/
│
├── local_models/
│ └── flan-t5-base/ # ⬅️ Place downloaded model files here
│ ├── config.json
│ ├── tokenizer.json
│ └── ... etc.
│
├── llm_bias_classifier.py # 🔍 Bias detection using LLM
├── rewrite_plot_without_bias.py# ✍️ Rewriter to remove gender bias
├── visualization.py # 📊 Matplotlib-based bar chart of bias
├── streamlit_app.py # 🎯 Main Streamlit web app
├── plot_rewriter.py # (Optional alternate rewrite logic)
├── generate_report.py # (Optional PDF export using WeasyPrint)
└── 00_requirements.txt # 📦 Dependencies list





## 🖼️ How It Works (Visual Workflow)

1. **User Input**  
   🎞️ Paste a Bollywood plot  
2. **Bias Detection**  
   🔍 Model detects sentences with gendered language  
3. **Bias Classification**  
   🧠 Automatically classifies bias types such as:
   - Emotional, Passive, Dominant, Submissive, Bossy, Breadwinner, Caretaker, etc.
4. **Bar Chart Generation**  
   📊 Bias counts are visualized  
5. **Rewriting the Plot**  
   ✍️ The model rephrases biased sentences in a more inclusive tone  
6. **Optional PDF Report**  
   📄 A downloadable summary of the original plot, analysis, and rewritten version




## 💡 Features

- ✅ **LLM-based classification** — Automatically recognizes gendered language without needing predefined keywords  
- ✅ **Local model inference** — No internet required once the model is downloaded  
- ✅ **20+ stereotype categories** supported  
- ✅ **Visual charts** make bias patterns easy to understand  
- ✅ **Rewriting engine** intelligently preserves meaning while neutralizing bias  




## 🚀 Future Scope

- 🧠 Upgrade to larger models like `flan-t5-xl` or `deepseek-coder`
- 📂 Add support for full-length scripts and CSV uploads
- 📝 Extend bias detection to **caste, religion, or regional stereotypes**
- 🎥 Adapt for **OTT content, TV shows, and Ads**
- 🧾 Enhance PDF report with charts and section-wise summaries

---

## ⚙️ Setup Instructions

1. Clone this repo
2. Download the model manually into:

/local_models/flan-t5-base/



3. Install dependencies:


pip install -r 00_requirements.txt
Run the app:

streamlit run streamlit_app.py

### Special thanks to DANIEL Sir at Docu3 for inspiring and guiding the development of this project. This tool wouldn't be possible without your insights.

