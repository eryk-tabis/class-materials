import re
with open("textfile.txt", "r") as file:
    text = file.read()
list_of_words = re.findall("\w{6,}",text)
for i in list_of_words:
    print(i)
