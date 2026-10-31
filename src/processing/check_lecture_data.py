
import json
from pathlib import Path

transcript_path = Path("data/processed/transcript.json")
metadata_path = Path("data/processed/frame_metadata.json")

# Check the transcript
with open(transcript_path, "r", encoding="utf-8") as file:
    transcript = json.load(file)

segments = transcript.get("segments", [])

print("===== TRANSCRIPT =====")
print("Total speech segments:", len(segments))

for segment in segments[:5]:
    print(
        f"[{segment['start']:.2f}s - {segment['end']:.2f}s] "
        f"{segment['text']}"
    )

# Check frame metadata
with open(metadata_path, "r", encoding="utf-8") as file:
    frames = json.load(file)

print("\n===== VIDEO FRAMES =====")
print("Total recorded frames:", len(frames))

for frame in frames[:5]:
    image_path = Path(frame["image_path"])
    print(
        f"Timestamp: {frame['timestamp']}s | "
        f"Image exists: {image_path.exists()} | "
        f"Path: {image_path}"
    )