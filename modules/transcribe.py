import speech_recognition as sr

def transcribe_audio(audio_path):
    """Transcribe audio using SpeechRecognition library."""
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as audio_file:
        audio_data = recognizer.record(audio_file)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results; {e}"
