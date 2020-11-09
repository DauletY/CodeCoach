passowrd = input()
repeat = input()

def validate(t1, t2):
    if t1 == t2:
        print("Correct")
    else:
        print("Wrong")

validate(passowrd, repeat)

# if passowrd == repeat:
#     print("Correct")
# else:
#     print("Wrong")
