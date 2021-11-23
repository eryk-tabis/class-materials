import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
summary = 0
for i in temperatures:
    summary += int(i)
print(summary/len(temperatures))
