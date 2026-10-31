
import cv2
from pathlib import Path

video_path = Path("data/input/lecture.mp4")
frames_dir = Path("data/frames")

frames_dir.mkdir(parents=True, exist_ok=True)

video = cv2.VideoCapture(str(video_path))

if not video.isOpened():
    raise RuntimeError("Could not open the lecture video.")

fps = video.get(cv2.CAP_PROP_FPS)
total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)

duration = total_frames / fps if fps > 0 else 0

print(f"Video duration: {duration:.2f} seconds")

interval = 10
timestamp = 0
saved_count = 0

while timestamp < duration:
    video.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)
    success, frame = video.read()

    if not success:
        print(f"Could not read frame at {timestamp} seconds.")
        timestamp += interval
        continue

    filename = frames_dir / f"frame_{timestamp:04d}.jpg"
    cv2.imwrite(str(filename), frame)

    print(f"Saved: {filename}")
    saved_count += 1
    timestamp += interval

video.release()

print(f"\nFrame extraction complete! Saved {saved_count} frames.")