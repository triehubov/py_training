#Регулярочка 2
import re

namein = str(input("Input component name:\n"))
name = re.search(r'\w\w\w\d\d-\w\d\d-\w\w\w\d\d', namein)

if name is not None:
    print("Valid component name: ", name.group())
else:
    print("Not valid name!")
