import os
from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_dir="data/extracted_audio"):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio_filename = os.path.basename(video_path).replace(".mp4", ".wav")
        audio_path = os.path.join(output_dir, audio_filename)
        audio.write_audiofile(audio_path)
        print(f"Extracted audio: {audio_path}")
    except Exception as e:
        print(f"Failed to extract audio from {video_path}: {e}")

if __name__ == "__main__":
    video_dir = "data/raw_videos"
    os.makedirs("data/extracted_audio", exist_ok=True)
    for video_filename in os.listdir(video_dir):
        video_path = os.path.join(video_dir, video_filename)
        extract_audio(video_path)