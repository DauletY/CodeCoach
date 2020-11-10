# RECURSION
def calc(list):
    sum = 0

    # Add every number in the list
    for i in range(0, len(list)):
        sum = sum * list[i]
    
    # return the sum
    return sum
    
    # if len(list)==1:
    #     return list[0]
    # else:
    #     return list[0] * calc(list[1:]) 

list = [1, 3, 4, 2, 5]
x = calc(list)        
print(x)
