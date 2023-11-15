import re
file_path = 'grossrents.txt'
with open(file_path, 'r') as file:
    text = file.read()
    pattern = re.compile(r'\b\d{2,4}\b')   
    matches = pattern.findall(text)
    print(matches)


# create a property class
class Property:
    def __init__(self, square_feet='', beds='',
            baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths
    



