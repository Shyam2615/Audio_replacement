import streamlit as st
from modules.audio_processing import extract_audio, replace_audio_in_video
from modules.transcribe import transcribe_audio
from modules.gpt_correction import correct_transcription
from modules.tts_generation import generate_speech

import os

# Set the Google Cloud credentials
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/google_credentials.json"


st.title("AI-Powered Video Voice Replacement")

video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if video_file:
    with open("static/uploaded_video.mp4", "wb") as f:
        f.write(video_file.read())

    st.write("Extracting audio from video...")
    audio_path = extract_audio("static/uploaded_video.mp4")

    st.audio('static/uploaded_video.mp4')

    st.write("Transcribing audio using Google Speech-to-Text...")
    transcript = transcribe_audio(audio_path)

    st.write(transcript)

    st.write("Correcting transcription using GPT-4...")
    corrected_transcription = correct_transcription(transcript)

    st.success(corrected_transcription)

    st.write("Generating new audio using pyttsx3...")
    generated_audio_path = generate_speech(corrected_transcription)

    st.audio(generated_audio_path)

    st.write("Replacing the original audio with the generated audio...")
    final_video_path = replace_audio_in_video("static/uploaded_video.mp4", generated_audio_path)

    st.write("Here's the final video with the AI-generated voice:")
    st.video(final_video_path)
