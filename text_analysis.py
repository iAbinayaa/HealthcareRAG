# text_analysis.py
import gradio as gr
from transformers import pipeline

# Load NER and text classification models
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
text_classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_text(text):
    # Extract entities for health-specific insights
    entities = ner(text)
    # Perform sentiment analysis to check emotional tone
    sentiment = text_classifier(text)
    return {"entities": entities, "sentiment": sentiment[0]["label"], "score": sentiment[0]["score"]}

# Gradio interface with enhanced output
interface = gr.Interface(fn=analyze_text, inputs="text", outputs="json", live=True)
interface.launch()
