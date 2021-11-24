import json
film = {
    "title": "Pulp Fiction",
    "director": "Quentin Tarantino",
    "scenario": "Quentin Tarantino",
    "year": 1994,
    "actors": ["Samuel L. Jackson", "John Travolta", "Uma Thurman"]
}
with open("favourite.json", "w") as file:
    json.dump(film, file, ensure_ascii=False, indent=4)
