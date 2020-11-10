# Bank card PIN system
pin = input()

try:
    x = int(pin)
    print('PIN code is created')
except ValueError:
    print('Please enter a number')