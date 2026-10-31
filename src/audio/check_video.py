from pathlib import Path

video_path = Path("data/input/lecture.mp4")

if video_path.exists():
    print("Video found!")
    print("File:", video_path)
    print("Size:", video_path.stat().st_size, "bytes")
else:
    print("Video not found!")