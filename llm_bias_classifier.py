from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

# Set up device and model
model_path = r"C:\Users\Bhuvana\OneDrive - vitbhopal.ac.in\Desktop\new_try\local_models\flan_t5_base"
print("Device set to use", "cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def analyze_plot_bias(plot_text):
    prompt = f"""
You are a gender bias and media stereotype detection expert.

Your job is to examine the plot of a Bollywood movie. For each sentence, evaluate if it contains gender bias or stereotyping. If yes, classify the type and explain it. Use one of these categories if possible:

- Female Stereotypes: emotional, submissive, dependent, nagging, weak, housewife, romanticized, passive, objectified, etc.
- Male Stereotypes: aggressive, dominant, stoic, controlling, rational-only, invulnerable, unemotional, etc.
- Biased Roles: caregiver, breadwinner, rescuer, seducer, villain, beauty object, protector, etc.
- Language Bias: manpower, chairman, bossy, shrill, assertive, etc.

Example output:
Sentence: "Kabir claims Preeti as his girlfriend in front of everyone."
Bias: Yes  
Type: Controlling / Possessive / Male Dominance  
Explanation: The sentence reinforces the idea that men can ‘own’ or claim women without consent.

Now analyze this plot step by step:
{plot_text}
"""
    # Same as before
    encoded = tokenizer(prompt, truncation=True, max_length=512, return_tensors="pt")
    input_text = tokenizer.decode(encoded["input_ids"][0])
    result = pipe(input_text, max_new_tokens=512, clean_up_tokenization_spaces=True)
    return result[0]["generated_text"]
