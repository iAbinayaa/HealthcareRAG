# image_analysis.py
import gradio as gr
from transformers import pipeline
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_id = os.getenv("EDAMAM_API_ID")
api_key = os.getenv("EDAMAM_API_KEY")

# Load a food detection model
image_classifier = pipeline("image-classification", model="nateraw/food")

def get_calories(food_item):
    # Fetch calorie data dynamically using the Edamam API
    url = f"https://api.edamam.com/api/food-database/v2/parser?ingr={food_item}&app_id={api_id}&app_key={api_key}"
    response = requests.get(url).json()
    
    # Extract calorie info
    if response.get("parsed"):
        calories = response["parsed"][0]["food"]["nutrients"]["ENERC_KCAL"]
        return calories
    else:
        return "N/A"

def analyze_image(image):
    # Classify the image to detect food items
    results = image_classifier(image)
    items = [result["label"] for result in results]
    calories_data = {item: get_calories(item) for item in items}
    return calories_data

# Gradio interface for the image analysis
interface = gr.Interface(fn=analyze_image, inputs="image", outputs="json", live=True)
interface.launch()
