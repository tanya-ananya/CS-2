import time

'''
Homework 2: Robots on Grids
Author: Taaruni Ananya
Program description: recursively computes the number of paths from the top-left to bottom-right square 
of an m x n grid with and without memoization.
'''


#  This function recursively computes without memoization
def num_paths(m, n):
    '''This base case will calculate if the robot is at the last step or has one step'''
    if m == 1 or n == 1:
        return 1
    '''This recursive case will get the sum of the paths from moving down or right'''
    return num_paths(m, n - 1) + num_paths(m - 1, n) 

#  This function recursively computes with memoization, by using a dictionary for a parameter and through recursion
def num_paths_memo(m, n, saved_dict = {}):
    # This base case will calculate if the robot is at the last step or has one step
    if m == 1 or n == 1:
        return 1
    # This will check if the value is already calculated and in saved_dict
    if (m,n) in saved_dict:
        return saved_dict[(m,n)]
    # This is the recursive case that will calculate the result, store it in saved_dict, and return it
    else:
        saved_dict[(m,n)] = num_paths_memo(m, n - 1, saved_dict) + num_paths_memo(m - 1, n, saved_dict)
    return saved_dict[(m,n)]

#driver code - you do not need to make any changes after this line.
#However, submit a screenshot of the output to report the execution time/elapsed time.
start_time = time.time()
print(num_paths(15,14))
end_time = time.time()

start_time_memo = time.time()
print(num_paths_memo(15,14))
end_time_memo = time.time()

print(f"Elapsed time (no memoization): {end_time - start_time} seconds")
print(f"Elapsed time (memoization): {end_time_memo - start_time_memo} seconds")