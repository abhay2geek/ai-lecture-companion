import json

lecture_title = input("Enter lecture title: ")
teacher_name = input("Enter teacher name: ")
subject = input("Enter subject: ")
lecture_date = input("Enter lecture date (DD-MM-YYYY): ")

transcript = {
    "lecture_title": lecture_title,
    "teacher_name": teacher_name,
    "subject": subject,
    "lecture_date": lecture_date,
}

with open(
    "data/processed/lecture_info.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(transcript, file, indent=4, ensure_ascii=False)