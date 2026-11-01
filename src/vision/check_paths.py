import cv2
from pathlib import Path

print("cv2 version:", cv2.__version__)

video_path = Path("data/input/lecture.mp4")
frames_dir = Path("data/frames")

print("\n--- video_path ---")
print("type:", type(video_path))
print("path:", video_path)
print("abolute:", video_path.resolve())
print("exists:", video_path.exists())
print("suffix:", video_path.suffix)
print("stem:", video_path.stem)

print("\n--- frames_dir ---")
print("type:", type(frames_dir))
print("exists:", frames_dir.exists())

print("\n--- joining ---")
joined = frames_dir / "frame_0000.jpg"
print("joined:", joined)

video = cv2.VideoCapture(str(video_path))
print("\n--- video opened? ---")
print("isopened:", video.isOpened())

fps = video.get(cv2.CAP_PROP_FPS)
total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("\n--- video properties ---")
print("fps:", fps)
print("total_frames:", total_frames)
print("width:", width)
print("height:", height)

if (fps>0):
    print("duration (s):", total_frames/fps)

video.release()

# video = cv2.VideoCapture(str(video_path))
# print("\n--- read frame at t=20s ---")
# video.set(cv2.CAP_PROP_POS_MSEC, 20*1000)
# success, frame = video.read()

# print("success:", success)
# print("type(frame):", type(frame))
# print("shape:", frame.shape if success else None)
# print("first pixel (top-left, BGR):", frame[0,0] if success else None)

# video.release()

from pathlib import Path

sample_files = sorted(Path("data/frames").glob("frame_*.jpg"))
print("\n--- frames on disk ---")
print("count:", len(sample_files))
print("first 5 names:", [p.name for p in sample_files[:5]])
print("last 3 names:", [p.name for p in sample_files[-3:]])
print("\n--- sizes (bytes) ---")
print("first file:", sample_files[0].stat().st_size if sample_files else None)
print("sizes vary across frames?",
      len({p.stat().st_size for p in sample_files}) > 1 if sample_files else None)
