import re
text ="To be, or not to be, that is the question"
vowels = re.findall("a|A|e|E|u|U|i|I|o|O",text)
print(len(vowels))
