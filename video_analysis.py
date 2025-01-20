# video_analysis.py
import gradio as gr
import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def analyze_video(video):
    cap = cv2.VideoCapture(video)
    pose_data = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        
        if results.pose_landmarks:
            pose_data.append(results.pose_landmarks.landmark)
    
    cap.release()
    return {"frames_analyzed": len(pose_data), "pose_data": pose_data}

# Gradio interface for the video analysis
interface = gr.Interface(fn=analyze_video, inputs="video", outputs="json", live=True)
interface.launch()
