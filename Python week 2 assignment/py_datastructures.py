# Initialize an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Modify the element at index 1
my_list[1] = 15

# Create another list list_2
list_2 = [50, 60, 70]

# Extend my_list with elements from list_2
my_list.extend(list_2)

# Delete the last element of my_list
del my_list[-1]

# Sort my_list in ascending order
my_list.sort()

# Find the index of the element 30 in my_list
index = my_list.index(30)
print(index)  # Output: 2

# Print the final sorted list
print(my_list)
