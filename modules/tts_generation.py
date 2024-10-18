from gtts import gTTS

def generate_speech(text):
    """Generate speech from corrected text using gTTS (online TTS)."""
    
    # Set up gTTS for generating speech
    tts = gTTS(text=text, lang='en', slow=False)  # slow=False for normal speed
    
    output_audio_path = "static/generated_speech.mp3"

    # Save speech to an audio file
    tts.save(output_audio_path)
    
    return output_audio_path
