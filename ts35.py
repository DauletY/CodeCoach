# List of multiples
# List comprehensions
x = int(input())

mul = [par for par in range(x) if par % 3 == 0 and par % 5 == 0 ]

print(mul)