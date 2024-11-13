'''
Write a Python program that handles the following five different types of built-in exceptions. Make sure to print a meaningful error message whenever an exception occurs.

	- TypeError
	- ValueError
	- KeyError
	- AttributeError
	- RecursionError

    Author: Taaruni Ananya
'''

print()
try:
    answer = 'four' + 4
except TypeError as err:
    print(f"TypeError raised -- {err}")

print()

try:
    answer = int('a string')
except ValueError as err:
    print(f"ValueError raised -- {err}")

print()

try:
    answer_dict = {'key': 'value'}
    value = answer_dict['a key']
except KeyError as err:
    print(f"KeyError raised -- {err}")

print()

try:
    none_type = None
    none_type.a_method()
except AttributeError as err:
    print(f"AttributeError raised -- {err}")

print()

try:
    def recursive_function():
        recursive_function()
    recursive_function()
except RecursionError as err:
    print(f"RecursionError raised -- {err}")
print()