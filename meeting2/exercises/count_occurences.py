# **Exercise:**
# Write a function `count_occurrences` that takes a list of strings as input and returns a dictionary
# where the keys are the unique strings from the list, and the values are the number of
# times each string appears in the list.
#
# **Example:**
# print(count_occurrences(["apple", "banana", "apple", "orange", "banana", "banana"]))
# # Output: {'apple': 2, 'banana': 3, 'orange': 1}
#
# print(count_occurrences(["cat", "dog", "cat", "cat", "dog"]))
# # Output: {'cat': 3, 'dog': 2}
#
# print(count_occurrences([]))
# # Output: {}
#
# **Requirements:**
# - Iterate over the list of strings.
# - Use a dictionary to keep track of the count of each unique string.
# - If a string is already in the dictionary, increment its value by 1.
# If it’s not in the dictionary, add it with a count of 1.
