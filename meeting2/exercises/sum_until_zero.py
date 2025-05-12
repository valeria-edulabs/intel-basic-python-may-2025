# **Exercise:**
# Write a function `sum_until_zero` that takes a list of integers as input and
# returns the sum of the numbers, stopping when a `0` is encountered in the list.
# The function should return the sum of all numbers before the first `0` (if a `0` exists).
#
# **Example:**
# print(sum_until_zero([1, 2, 3, 0, 5]))   # Output: 6
# print(sum_until_zero([10, 5, 0, 2]))     # Output: 15
# print(sum_until_zero([1, 2, 3]))         # Output: 6
# print(sum_until_zero([0, 5, 6]))         # Output: 0
#
# **Requirements:**
# - Use a `while` loop to iterate through the list until a `0` is encountered.
# - Return the sum of the numbers encountered before the `0`.
#
