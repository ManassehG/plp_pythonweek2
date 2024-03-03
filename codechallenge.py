# Accept user input to create a list of integers
integer_list = [int(x) for x in input("Enter integers separated by spaces: ").split()]

# Compute the sum of all integers in the list
total_sum = sum(integer_list)

# Print the sum
print("Sum of integers:", total_sum)


# Tuple containing names of five favorite books
favorite_books = ("Book1", "Book2", "Book3", "Book4", "Book5")

# Print each book name on a separate line using a for loop
for book in favorite_books:
    print(book)


# Create an empty dictionary to store person's information
person_info = {}

# Ask for user input and store information in the dictionary
person_info['name'] = input("Enter name: ")
person_info['age'] = int(input("Enter age: "))
person_info['favorite_color'] = input("Enter favorite color: ")

# Print the dictionary
print(person_info)


# Accept user input to create two sets of integers
set1 = set(map(int, input("Enter integers separated by spaces for set 1: ").split()))
set2 = set(map(int, input("Enter integers separated by spaces for set 2: ").split()))

# Create a new set containing elements common to both sets
common_elements = set1.intersection(set2)

# Print the new set
print("Common elements:", common_elements)


# Store a list of words
word_list = ["apple", "banana", "orange", "kiwi", "pineapple"]

# Use list comprehension to create a new list with words having odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Print the new list
print("Words with odd number of characters:", odd_length_words)
