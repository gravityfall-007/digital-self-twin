from pytube import YouTube, Playlist
import os

def download_video(video_url, output_dir="data/raw_videos"):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        stream.download(output_dir)
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Failed to download {video_url}: {e}")

def download_playlist(playlist_url, output_dir="data/raw_videos"):
    playlist = Playlist(playlist_url)
    print(f"Downloading {len(playlist.video_urls)} videos from the playlist...")
    for video_url in playlist.video_urls:
        download_video(video_url, output_dir)

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list"
    download_playlist(playlist_url)