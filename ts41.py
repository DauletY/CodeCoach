# Decorators

def decor(func):
    def wrap():
        print('###')
        func()
        print('###')
    return wrap

def print_bill():
    print('DAULET DATA GOES HERE')
decorated = decor(print_bill)
decorated()