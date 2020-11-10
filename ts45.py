# Contacts database
import re


x = input() 

if x[:2] == '00':
    print(re.sub(r'00',"+",x))
else:
    print(x)