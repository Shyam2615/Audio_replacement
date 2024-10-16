import pyttsx3

def generate_speech(text):
    """Generate speech from corrected text using pyttsx3 (offline TTS)."""
    engine = pyttsx3.init()

    # Set properties for voice (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    output_audio_path = "static/generated_speech.mp3"

    # Save speech to an audio file
    engine.save_to_file(text, output_audio_path)
    engine.runAndWait()

    return output_audio_path
