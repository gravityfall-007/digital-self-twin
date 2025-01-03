import os
from download_youtube_videos import download_playlist
from extract_audio import extract_audio
from transcribe_audio import transcribe_audio

def run_pipeline(playlist_url):
    # Step 1: Download videos
    print("Downloading videos...")
    download_playlist(playlist_url)

    # Step 2: Extract audio
    print("Extracting audio...")
    video_dir = "data/raw_videos"
    os.makedirs("data/extracted_audio", exist_ok=True)
    for video_filename in os.listdir(video_dir):
        video_path = os.path.join(video_dir, video_filename)
        extract_audio(video_path)

    # Step 3: Transcribe audio
    print("Transcribing audio...")
    audio_dir = "data/extracted_audio"
    os.makedirs("data/transcribed_text", exist_ok=True)
    for audio_filename in os.listdir(audio_dir):
        audio_path = os.path.join(audio_dir, audio_filename)
        transcribe_audio(audio_path)

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PL1n30s-LKus5uOY2xbRjAx_wPHnKvy_aW"
    run_pipeline(playlist_url)