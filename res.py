#Регулярочка 1
import re

ipin = str(input("Input IP here\n"))
match = re.search(r"^((25[0-5]|2[0-4]\d|[01]?[0-9][0-9]?)(\.)){3}(25[0-5]|2[0-4]\d|[01]?[0-9][0-9]?)$", ipin)

if match is not None:
    print("Valid IP: ", match.group())
else:
    print("Is not an IP")
