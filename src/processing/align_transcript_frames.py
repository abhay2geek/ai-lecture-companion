import json 
from pathlib import Path

#--- Load inputs ---
with open("data/processed/transcript.json", encoding="utf-8") as f:
    transcript = json.load(f)
with open("data/processed/frame_metadata.json", encoding="utf-8") as f:
    frames = json.load(f)

segments = transcript['segments']

# --- Build the alignment ---
alignment = []

for seg in segments:
    midpoint = (seg['start'] + seg['end'])/2
    # Gives segments centre

    # Closest frame to the segment's midpoint
    best_frame = min(
        frames,
        key = lambda fr: abs(fr["timestamp"] - midpoint)
    )
    # It helps to find the frame that is closest to the midpoint of the segment.
    distance = abs(best_frame["timestamp"] -midpoint)

    alignment.append({
        "segment": {
        "start": seg["start"],
        "end": seg["end"],
        "text": seg["text"]
    },
    "frame": {
        "timestamp": best_frame["timestamp"],
        "image_path": best_frame["image_path"]
    },
    "distance_s": round(distance, 2)
    })

# --- Save ---
output_path = Path("data/processed/alignment.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(alignment, f, indent=4, ensure_ascii=False)

print(f"Alignment saved to: {output_path}")
print(f"Total segments aligned: {len(alignment)}\n")
print("First 5 alignments:")
for a in alignment[:5]:
    print(
        f" [{a['segment']['start']:>6.1f}s - {a['segment']['end']:>6.1f}s] "
        f" ->frame {a['frame']['timestamp']:>3}s"
        f" (distance {a['distance_s']:>4}s) | {a['segment']['text'][:45]}..."
    )