#Регулярочка 1
import re

ipin = str(input("Input IP here\n"))
match = re.search(r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?', ipin)
if match is not None:
    ipspl = (match.group()).split('.')
    for i in ipspl:
        if int(i) > 255:
            print("Not Valid IP")
            break
    print("Valid IP: ", match.group())
else:
    print("Is not an IP")