import json

student = {
    "name": "Eryk",
    "surname": "Tabiś",
    "age": 20,
    "isMale": True,
    "hobbies": ["programming","music", "movies"]
}
with open("student.json", "w") as file:
    json.dump(student, file, ensure_ascii=False, indent=4)
