import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from peft import PeftModel


model_id = "pranalibose/flan-t5-base"  # Your model ID on the Hub

# 1. Load the base model (T5 in this case)
base_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")  # Or whatever your base model is

# 2. Load the PEFT model using the base model and the model_id
model = PeftModel.from_pretrained(base_model, model_id)

tokenizer = AutoTokenizer.from_pretrained(model_id, local_files_only=False)

def generate_resume_feedback(resume_text, instruction, model, tokenizer, max_input_length=512, max_output_length=128):
    """
    Generates feedback for a resume based on an instruction using a pre-trained model.

    Args:
        resume_text (str): The text of the resume.
        instruction (str): The instruction for feedback generation.
        model (PreTrainedModel): The pre-trained model for generation.
        tokenizer (PreTrainedTokenizer): The tokenizer corresponding to the model.
        max_input_length (int, optional): Maximum length for the input sequence. Defaults to 512.
        max_output_length (int, optional): Maximum length for the generated feedback. Defaults to 128.

    Returns:
        str: The generated feedback.  Returns an empty string if there's an issue.
    """
    try:
        inputs = tokenizer(
            f"Instruction: {instruction}\nResume: {resume_text}",
            return_tensors="pt",
            max_length=max_input_length,
            truncation=True,
            padding="max_length"
        ).to(model.device)  # Move input to the model's device

        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=max_output_length
        )

        generated_feedback = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_feedback

    except Exception as e:  # Handle potential errors
        print(f"Error during feedback generation: {e}")
        return ""  # Return empty string in case of error

# Streamlit app layout
st.title("Resume Feedback Generator")
st.write("Enter your resume and custom instructions below:")

# Input fields
resume = st.text_area("Resume:", height=100)
instruction = st.text_input("Custom Instruction:")

if st.button("Get Feedback"):
    if resume and instruction:
        feedback = generate_resume_feedback(resume, instruction, model, tokenizer)
        st.write("**Feedback:**")
        st.write(feedback)
    else:
        st.warning("Please provide both a resume and a custom instruction.")
