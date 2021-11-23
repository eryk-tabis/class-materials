import re
text = "To be, or not to be, that is the question"
list_of_words = re.findall("\w{1,}", text)
print(len(list_of_words))
