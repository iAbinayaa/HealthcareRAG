
# HealthRAG Coach Assistant

**HealthRAG Coach Assistant** is an AI-driven, multi-modal health and fitness advisor that leverages Retrieval-Augmented Generation (RAG) technology. The assistant provides personalized guidance based on text, images, audio, and video inputs, making it an all-in-one solution for tracking and improving health and fitness.

## Features

- **Text Analysis**: Analyzes health records and text inputs for relevant information and provides insights on fitness goals and dietary preferences.
- **Image Analysis**: Uses food image classification and a nutrition database API to dynamically estimate calorie intake.
- **Audio Input**: Transcribes voice inputs and interprets user goals using NLP, making it easy to track diet or fitness needs.
- **Video Analysis**: Basic pose detection for posture and exercise form analysis, providing instant feedback on workouts.



## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/PravinRF7/HealthRAG-Coach-Assistant.git
   cd HealthRAG-Coach-Assistant
   ```

2. **Install Requirements**

   ```bash
   pip install -r reequirements.txt
   ```

3. **Set Up Environment Variables**

   - Create a `.env` file in the project directory and add your API keys (e.g., Edamam API keys):
   
   ```plaintext
   EDAMAM_API_ID=your_edamam_api_id
   EDAMAM_API_KEY=your_edamam_api_key
   ```

4. **Run the Application**

   - To run the complete application:
   
     ```bash
     python main.py
     ```


