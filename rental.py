import re
file_path = 'grossrents.txt'
with open(file_path, 'r') as file:
    text = file.read()
    pattern = re.compile(r'\b\d{2,4}\b')   
    matches = pattern.findall(text)
    print(matches)

class Property:
    