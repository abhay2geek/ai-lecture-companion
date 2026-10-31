import json

with open(
    "data/processed/test_transcript.json",
    "r",
    encoding="utf-8"
) as file:
    transcript = json.load(file)

print("Lecture:", transcript["lecture_title"])
print("\nTranscript:")

for segment in transcript["segments"]:
    print(
        f"[{segment['start']} - {segment['end']}] "
        f"{segment['text']}"
    )