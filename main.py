# main.py
import gradio as gr
from text_analysis import analyze_text
from image_analysis import analyze_image
from audio_analysis import analyze_audio
from video_analysis import analyze_video

# Enhanced Gradio interface with multi-modal input
interface = gr.Interface(
    fn=[analyze_text, analyze_image, analyze_audio, analyze_video],
    inputs=["text", "image", "audio", "video"],
    outputs=["json", "json", "json", "json"],
    live=True,
    title="Health Coach Assistant",
    description="An AI Assistant for health and fitness guidance using text, image, audio, and video analysis."
)

interface.launch()
