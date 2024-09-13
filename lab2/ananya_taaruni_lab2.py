def most_occuring(nums):
    nums_dict = {}
    for x in nums:
        if x not in nums_dict:
            nums_dict[x] = 1
        else:
            nums_dict[x] += 1
    most = 0
    for value in nums_dict.values():
        if value > most:
            most = value
    
    nums_list = []
    for key, value in nums_dict.items():
        if value == most:
            nums_list.append(key)
    
    return min(nums_list)

print()
first_input = [1,3,5,4,1,1]
print('Most Occuring Function Outputs -- ')
print(f'First Input: {first_input}')
print(most_occuring(first_input))
print()
second_input = [5,3,5,4,4,1]
print(f'Second Input: {second_input}')
print(most_occuring(second_input))
print()

def longest_sequence(numbers):
    current_item = 0
    count = 0
    numbers_list = []
    for x in range(len(numbers)):
        if numbers[x] != current_item:
            numbers_list.append(count)
            current_item = numbers[x]
            count = 1
        else:
            count += 1
        numbers_list.append(count)
    return max(numbers_list)
    
input_first = [1,2,3,4,4,2,2,2]
print('Longest Sequence Function Outputs -- ')
print(f'First Input: {input_first}')
print(longest_sequence(input_first))
print()
input_second = [1,2,3,4,5]
print(f'Second Input: {input_second}')
print(longest_sequence(input_second))
print()