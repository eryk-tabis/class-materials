import json
all_data = []
with open("students.json", "r") as file, open("limited.json", "w") as file2:
    data = json.load(file)

    for i in range(len(data)):
        data2 = {
            "first name": data[i]["name"],
            "last name": data[i]["surname"],
            "student id": data[i]["studentID"],
        }
        all_data.append(data2)
    json.dump(all_data,file2, ensure_ascii=True, indent=4)
