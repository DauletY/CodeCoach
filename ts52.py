# else with for

persons_ages = []

i = 0

while i < 3:
  per_age = int(input())
  persons_ages.append(per_age)
  if(per_age < 16):
      print('Too young!')
      break
  i += 1
else:
    print('Get ready!')