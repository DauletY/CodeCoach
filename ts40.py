# Split generator
txt = input()
sp = txt.split(' ')
def words():
    for i in sp:
        yield i

print(list(words()))