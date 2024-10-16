from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.fx.all import audio_fadein, audio_fadeout

def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = "static/extracted_audio.wav"
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')
    return audio_path


def replace_audio_in_video(video_path, new_audio_path):
    """
    Replace the audio in a video with the new generated audio.
    
    Args:
        video_path (str): The path to the original video file.
        new_audio_path (str): The path to the new audio file.
    
    Returns:
        str: The path to the final video file with replaced audio.
    """
    # Load the video
    video = VideoFileClip(video_path)
    
    # Load the new audio
    new_audio = AudioFileClip(new_audio_path)  # Use AudioFileClip for audio

    # Set the new audio to the video
    final_video = video.set_audio(new_audio)

    # Define the output path for the final video
    final_output_path = "output/final_output_video.mp4"

    # Write the final video file with the new audio
    final_video.write_videofile(final_output_path, codec="libx264", audio_codec="aac")

    return final_output_path

