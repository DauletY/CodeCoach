# Hashtag generator
s = input()

def hashtagGen(text):
    text = text.replace(' ','')
    hash = '#'
    hash += text
    return hash
    
print(hashtagGen(s))