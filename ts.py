hour = int(input())
day = int(input())

if hour >= 10 and hour <= 21 and day >= 1 and day <= 5:
    print('Open')
else:
    print('Colsed')