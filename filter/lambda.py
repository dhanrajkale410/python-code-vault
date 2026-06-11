# Below example uses a lambda function with filter() to select numbers divisible by 3.
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 3 == 0, a)
print(list(b))