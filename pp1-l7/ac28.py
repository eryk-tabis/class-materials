import re
with open("grades.txt", "r") as file:
    text = file.read()
list_of_grades = re.findall("\d.\d", text)
summary = 0
for i in list_of_grades:
    summary += float(i)
print(summary/len(list_of_grades))
