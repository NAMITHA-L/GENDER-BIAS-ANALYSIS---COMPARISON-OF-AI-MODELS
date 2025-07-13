from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# ✅ Local FLAN-T5 model path
model_path = "C:/Users/Bhuvana/OneDrive - vitbhopal.ac.in/Desktop/new_try/local_models/flan_t5_base"

print("Device set to use", "cuda" if torch.cuda.is_available() else "cpu")

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# Define pipeline
rewrite_pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def rewrite_plot_without_bias(plot_text):
    prompt = f"""
    The following Bollywood movie plot may contain gender bias, stereotypes, or unequal representations of male and female characters.

    Your task is to rewrite it to be more inclusive and free from bias. 
    - Remove or rephrase stereotypical labels (e.g., “aggressive”, “submissive”, “emotional”, “dominant”).
    - Balance character roles without changing the overall story or plot points.
    - Retain the original meaning, setting, and narrative flow.

    Plot:
    {plot_text}

    Rewritten Bias-Free Plot:
    """

    # Truncate if needed for FLAN-T5 (max 512 tokens)
    max_input_tokens = 512
    encoded = tokenizer(prompt, truncation=True, max_length=max_input_tokens, return_tensors="pt")
    input_text = tokenizer.decode(encoded["input_ids"][0])

    # Generate rewritten plot
    result = rewrite_pipe(input_text, max_new_tokens=512, clean_up_tokenization_spaces=True)

    # Remove prefix if model echoes the prompt
    rewritten = result[0]["generated_text"].replace(prompt.strip(), "").strip()

    return rewritten
