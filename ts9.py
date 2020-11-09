import re


id = input()

pattern = r"[A-Z]+[^A-Z][0-9]$"
# # value = int(id)
# if '$1234'.isdecimal():
#     print('Yes number')
# else:
#     print('No number')


if re.search(pattern, id):
        print("Searching")
else:
    print("Wrong format")
