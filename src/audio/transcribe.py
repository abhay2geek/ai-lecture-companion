import json
import whisper


print("Loading Whisper model...")

model = whisper.load_model("base")

print("Whisper model loaded successfully!")

result = model.transcribe("data/audio/lecture.wav")

segments = []

for segment in result["segments"]:
    segments.append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"].strip()
    })

transcript = {
    "segments": segments
}

with open(
    "data/processed/transcript.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(transcript, file, indent=4, ensure_ascii=False)

print("\nTranscript saved successfully!")
print("File: data/processed/transcript.json")