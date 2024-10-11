# Open the words file and read the contents into a list
print()
file = open('lab7_words.txt', 'r')
words = file.read().splitlines()
print('# words read:', len(words))
print()
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        
        if arr[mid] == target:
            print(f'Target = {target}, Found at index = {mid}, Number of iterations = {iterations}')
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    print(f'Target = {target}, Found at index = -1, Number of iterations = {iterations}')
    return -1

target = input('Enter search key: ').lower()

while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()

file.close()
