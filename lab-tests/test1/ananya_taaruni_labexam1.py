'''
THis program will perform ternary search with three divided lists to search for the index of a target.
Author: Taaruni Ananya
'''

def ternary_search(arr, target, low=0, high=None):
    if high is None: # Checks to see if there is a value for high given by the input and if not, finds the value by calculating the lngth
        high = len(arr) - 1
    if low > high: # CHecks to see if the low's value is higher in order to determine array's length and values
        return -1  
    point = (high - low) // 3 # Divides and finds the points to split the array in three
    mid1 = low + point # Creates a point for the first third
    mid2 = high - point # Creates a point for the third part of the list
    
    if arr[mid1] == target:
        return mid1
    elif arr[mid2] == target:
        return mid2
    elif target < arr[mid1]: # Checks the first part of the arrary before md1
        return ternary_search(arr, target, low, mid1 - 1)
    elif target > arr[mid2]: # CHescks the third part of the array after mid2
        return ternary_search(arr, target, mid2 + 1, high)
    else: # Checks the middle oart of the array in between mid1 and mid2
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)


'''The following will be inputs and print statements'''
print()
input1 = [1, 4, 5, 6, 7, 8, 9, 11, 17, 202, 231, 333, 339, 443]
print('First list input: ', input1)
target1 = 11
print("Target = ", target1)
print("Output = ", ternary_search(input1, target1))
print()
input2 = [1, 4, 5, 6, 7, 9, 11, 17, 202, 231, 333, 339, 443]
print('Second list input: ', input2)
target2 = 111
print("Target = ", target2)
print("Output = ", ternary_search(input1, target2))
print()