import whisper

print("Loading Whisper model...")
model = whisper.load_model("base")
print("Model loaded.\n")

print("Transcribing...")
result = model.transcribe("data/audio/lecture.wav")
print("Transcription done.\n")

print("--- TYPE OF result ---")
print(type(result))

print("\n--- KEYS OF result ---")
print(result.keys())

print("\n--- VALUE OF result['text'] ---")
print(result["text"])

print(type(result["text"]))
print(len(result["text"]))

print("\n--- TYPE OF result['segments'] ---")
print(type(result["segments"]))

print("\n--- NUMBER OF SEGMENTS ---")
print(len(result["segments"]))

print("\n--- FIRST SEGMENT (segment 0) ---")
print(result["segments"][0])

first = result["segments"][0]

print("\n--- FIELDS OF FIRST SEGMENT ---")
print("start:", first["start"])
print("end:  ", first["end"])
print("text: ", first["text"])
print("duration:", first["end"] - first["start"])

segments = []

for segment in result["segments"]:
    segments.append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"].strip()
    })

print("\n--- AFTER THE LOOP ---")
print("type(segments):", type(segments))
print("len(segments): ", len(segments))
print("first item:    ", segments[0])
print("first text:    ", segments[0]["text"])

import json
from pathlib import Path

test_path = Path("data/processed/transcript_local_test.json")

transcript = {"segments": segments}

with open(test_path, "w", encoding="utf-8") as file:
    json.dump(transcript, file, indent=4, ensure_ascii=False)

print("\n--- SAVED ---")
print("File:", test_path)
print("Exists:", test_path.exists())
print("Size (bytes):", test_path.stat().st_size)

with open(test_path, "r", encoding="utf-8") as file:
    loaded = json.load(file)

print("\n--- LOADED BACK ---")
print("type(loaded):", type(loaded))
print("keys:", loaded.keys())
print("len(loaded['segments']):", len(loaded["segments"]))
print("first item:", loaded["segments"][0])
print("first item's keys:", loaded["segments"][0].keys())