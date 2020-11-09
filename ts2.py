#Social media pre
#Spacial Sequences
import re

text = input()
lists = text.split(" ")

for l in lists:
    if(re.findall(r'#\w+', l)):
        print(l)
   


