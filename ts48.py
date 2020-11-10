text = input()

def uppercase_decorator(func):
    def wrapper(text):
        #your code goes here
        print(text)
    return wrapper
    
@uppercase_decorator    
def display_text(text):
    return text
    
display_text(text.upper())
