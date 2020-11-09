# More Metacharacters
import re

password = input()
# if(re.match(text, text.upper()) and re.match(text,str(1))):
#    print(text)

pattern = r"[A-Z]+[a-z]*[0-9]+"
if(re.search(pattern, password)):
    print("Password created")
else:
    print ("Wrong format")