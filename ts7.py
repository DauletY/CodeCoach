names = ["David", "John", "Anna", "Johnathan", "Veronica"]

res = list(filter(lambda x: x != 'David' and x != 'John',
 names))
print(res)