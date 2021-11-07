def count_letter(letter, text):
    count = 0
    for i in text:
        if i == letter:
            count += 1
    return count


print(count_letter("e", "You never get a second chance to make a first impression"))
