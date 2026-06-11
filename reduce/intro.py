# reduce(lambda x, y: x + y, a) adds elements step-by-step ((2 + 4) + 6) + 8 = 20.

from functools import reduce
a = [2, 4, 6, 8]
r = reduce(lambda x, y: x + y, a)
print(r)

# lambda x, y: x if x > y else y compares two values at each step and keeps the larger one, resulting in the maximum value 12.
b = [5, 9, 3, 12, 7]
res = reduce(lambda x, y: x if x > y else y, b)
print(res)