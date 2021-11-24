#TODO
import json
with open("students.json", "r") as file, open("limited.json", "w") as file2:
    data = json.load(file)
    data2 = {
        "name": data["name"],
        "surname": data["surname"],
        "studentID": data["studentID"],
        "gender": data["gender"],
        "age": data["age"],
        "year of study": data["year of study"]
    }
    json.dump(file2,data2)
