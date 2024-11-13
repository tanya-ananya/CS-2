import numpy as np

'''
Attendance 11/12
Author: Taaruni Ananya
'''

# Task One
array = np.arange(11)
odd_numbers = array[array % 2 != 0]
greater_than_two = array[array > 2]
print("Array:", array)
print("Odd numbers:", odd_numbers)
print("Numbers greater than 2:", greater_than_two)


# Task two
ans_array = np.arange(100, 200, 10).reshape(5, 2)
print("5x2 array:\n", ans_array)


# Task Three
Arr = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
third_column = Arr[:, 2]
print("Third column from all rows:", third_column)


#Task Four
sampleArray = np.array([[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])
result = sampleArray[0:3, 1:4]
print("Array of items from second to fourth column, first to third row:\n", result)


# Task Five
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

sorted_by_row = np.sort(sampleArray, axis=1)
print("Array sorted by each row:\n", sorted_by_row)

sorted_by_column = np.sort(sampleArray, axis=0)
print("Array sorted by each column:\n", sorted_by_column)