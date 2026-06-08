my_list = [1, 2, 3]

print(my_list)  # Output: [1, 2, 3]

my_list.append(4)   
print(my_list)  # [1, 2, 3, 4]

my_list.insert(1, 99)  
print(my_list)  # [1, 99, 2, 3, 4]

my_list.remove(2)   
print(my_list)  # [1, 99, 3, 4]

my_list.pop()      
print(my_list)  # [1, 99, 3]

my_list.reverse()   
print(my_list)  # [3, 99, 1]

my_list.sort()  
print(my_list)  # [1, 3, 99]