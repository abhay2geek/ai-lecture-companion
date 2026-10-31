
import cv2
import json
from pathlib import Path

video_path = Path("data/input/lecture.mp4")
frames_dir = Path("data/frames")
output_path = Path("data/processed/frame_metadata.json")

video = cv2.VideoCapture(str(video_path))

if not video.isOpened():
    raise RuntimeError("Could not open the lecture video.")

fps = video.get(cv2.CAP_PROP_FPS)
video.release()

if fps <= 0:
    raise RuntimeError("Could not determine the video's FPS.")

frame_metadata = []

for image_path in sorted(frames_dir.glob("frame_*.jpg")):
    # The filename contains the timestamp in seconds.
    timestamp = int(image_path.stem.replace("frame_", ""))

    frame_metadata.append({
        "timestamp": timestamp,
        "image_path": str(image_path).replace("\\", "/")
    })

output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(frame_metadata, file, indent=4, ensure_ascii=False)

print(f"Metadata saved to: {output_path}")
print(f"Total frames recorded: {len(frame_metadata)}")

if frame_metadata:
    print("First frame:", frame_metadata[0])