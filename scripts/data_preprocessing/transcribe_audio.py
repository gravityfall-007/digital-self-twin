import whisper
import os

def transcribe_audio(audio_path, output_dir="data/transcribed_text"):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        text_filename = os.path.basename(audio_path).replace(".wav", ".txt")
        text_path = os.path.join(output_dir, text_filename)
        with open(text_path, "w") as f:
            f.write(result["text"])
        print(f"Transcribed: {text_path}")
    except Exception as e:
        print(f"Failed to transcribe {audio_path}: {e}")

if __name__ == "__main__":
    audio_dir = "data/extracted_audio"
    os.makedirs("data/transcribed_text", exist_ok=True)
    for audio_filename in os.listdir(audio_dir):
        audio_path = os.path.join(audio_dir, audio_filename)
        transcribe_audio(audio_path)