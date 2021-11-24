import json

with open("filename.json", encoding="UTF-8") as file:
    data = json.load(file)

for k,v in data.items():
    print(k,":",v)
