import json

with open(
    "data/processed/lecture_info.json",
    "r",
    encoding="utf-8"
) as file :
    lecture_info = json.load(file)

print("Lecture Title:", lecture_info["lecture_title"])
print("Teacher Name:", lecture_info["teacher_name"])
print("Subject:", lecture_info["subject"])
print("Lecture Date:", lecture_info["lecture_date"])