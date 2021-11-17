film_titles = ["Pulp Fiction", "Dogs day afternoon", "Matrix", "Die hard", "Leon The Professional"]
with open("dc11.txt", "w") as file:
    for i in film_titles:
        file.write(i+"\n")
