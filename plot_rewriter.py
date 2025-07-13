from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

# ✅ Reuse the same local model
model_path = r"C:\Users\Bhuvana\OneDrive - vitbhopal.ac.in\Desktop\new_try\local_models\flan_t5_base"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def rewrite_plot_without_bias(plot_text):
    prompt = f"""
    Rephrase the following Bollywood movie plot to remove any gender bias.
    Preserve the meaning but eliminate stereotypical or biased language.

    Plot: {plot_text}
    """
    result = pipe(prompt, max_new_tokens=512)
    return result[0]['generated_text']
