#Регулярочка 1
import re

ipin = str(input("Input IP here\n"))
match = re.search(r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?', ipin)

if match is not None:
    print("Valid IP: ", match.group())
else:
    print("Is not an IP")
