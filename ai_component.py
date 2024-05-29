from transformers import pipeline

# Load a pre-trained model and tokenizer
chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

def get_response(input_text):
    return chatbot(input_text)[0]['generated_text']
