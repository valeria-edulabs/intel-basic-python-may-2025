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

def count_occurrences(lst):
    count_dict = {}

    # Iterate over each string in the list
    for item in lst:
        if item in count_dict:
            # If the string is already in the dictionary, increment its count
            count_dict[item] += 1
            # count_dict[item] = count_dict[item] + 1
        else:
            # If the string is not in the dictionary, add it with count 1
            count_dict[item] = 1

    return count_dict


result = count_occurrences(["cat", "dog", "cat", "cat", "dog"])
print(result)