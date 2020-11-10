# how old will they be?
import math
birth_years = [1991, 1995, 2004, 2006, 2010, 2015,2019, 1988, 1977, 1902]
result = list(map(lambda x: int(math.fabs(x-2050)), birth_years))
print(result)
