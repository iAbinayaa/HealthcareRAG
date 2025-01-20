# audio_analysis.py
import gradio as gr
import speech_recognition as sr
from transformers import pipeline

# Initialize recognizer and zero-shot classification model
recognizer = sr.Recognizer()
goal_analyzer = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_audio(audio):
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    # Intent classification for fitness or diet goals
    labels = ["fitness goal", "diet goal", "health concern", "general inquiry"]
    goal_analysis = goal_analyzer(text, candidate_labels=labels)
    return {"transcription": text, "goal_analysis": goal_analysis}

# Gradio interface with enhanced output and live updates
interface = gr.Interface(fn=analyze_audio, inputs="audio", outputs="json", live=True)
interface.launch()
