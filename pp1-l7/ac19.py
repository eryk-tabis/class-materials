with open("MeatAndFish.txt", "r") as file_read1, open("GrainsAndBread.txt", "r") as file_read2, open("shoppinglist.txt", "w") as file_write:
    file_write.write(file_read1.read())
    file_write.write(file_read2.read())
    