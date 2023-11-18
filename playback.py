text = "welcome to the jungle"

# import re

def replace_spaces(text):
    return re.sub(r"\s+", "...", text)

text = input("Enter a string: ")
new_text = replace_spaces(text)
print(new_text)
