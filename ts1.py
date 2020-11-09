# num = int(input())

def EvenOrOdd(n):
    if(n == 0):
        return 0
    if n % 2 == 0 and n % 2 != 0:
        return n + 3
    else:
        return n + 2

def EvenOdd(n):
    if (n == 0):
        return 0
    if n % 2 != 0:
        return n + 2
    elif n % 2 == 0:
        return  n + 2
        
def EvenOROdd(n):

    if n % 2 == 0 or n == 1:
        return n * 3
    else:
        return n * 2
#print(EvenOROdd(num))

num = input()

n = (int(num) % 2)

if(n == 1):
    print (int(num)*3)
else:
    print (int(num)*2)
