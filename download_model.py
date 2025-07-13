from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_id = "google/flan-t5-base"

# Set the folder to save model and tokenizer
save_dir = "local_models/flan-t5-base"

# Download and save tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.save_pretrained(save_dir)

# Download and save model
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
model.save_pretrained(save_dir)
