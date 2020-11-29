
var1 = int(input())
string = input()
spt = string.split(' ')

for i in spt:
    if var1 % int(i) == 0:
       print("divisible by all")
       break
    else:
        print('not divisible by all')
        break

