'''
Task 1
Program: The program simulates the "One Potato, Two Potato" counting-out game using a circular
linked list, where n participants are eliminated in steps of k until only one remains.
It defines a Node class to represent each participant and constructs a circular linked
list to facilitate the elimination process. The function ultimately returns the index
of the last remaining participant.
Author: Taaruni Ananya
'''

print('Task 1 --')
class Node: # This class will handle creating nodes for the game
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# This function takes in the inputs to calculate through the game and return the winner
def potato(n, k):
    if n == 1: # This edge case tests to see if there's only one person, returns 0 if yes
        return 0

    # The following lines of code will create nodes for each player and add them to a list to keep track
    nodes_list = []
    for x in range(n):
        nodes_list.append(Node(x))
    for a in range(n-1):
        nodes_list[a].next = nodes_list[a+1]
    nodes_list[n-1].next = nodes_list[0] # This line of code keeps the nodes list circular, ensuring that the correct values at index k are removed
    
    # The following lines of code will eliminate nodes until only one remains
    while n > 1:
        previous = None
        current = nodes_list[0]
        for index in range(k-1):
            previous = current
            current = current.next

        # The next two lines of code will eliminate the current node
        previous.next = current.next
        current = previous.next
        n -= 1 # This will decrement the number of people left in the game
    return current.value # This will return the value of the last remaining node

'''Test Cases'''
print(potato(10, 7))
print(potato(5, 4))
print(potato(1, 1)) # This test returns 0 since there's only one person

print()
print('Task 2 --')
'''
Task 2

Program: This program defines a binary tree structure and includes a function that calculates
the height, number of leaf nodes, and checks if the tree is full and balanced. It outputs these
characteristics for a predefined binary tree.
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_info(node):
    if node is None: # Edge case, tests to see if node is None and returns default values
        return 0, 0, False, False

    # The following tow lines of code unzip and assign each corresponding variable to a recursive function of the nodes
    right_tree_height, right_tree_leaves, right_tree_full, right_tree_balanced = tree_info(node.right)
    left_tree_height, left_tree_leaves, left_tree_full, left_tree_balanced = tree_info(node.left)

    height = 1 + max(right_tree_height, left_tree_height) # Finds the maximum of both right and left tree height and adds one to find height

    if node.left is None and node.right is None: # After recursion, if there aren't any other leaves
        leaves = 1
    else: # If there are other leaves, based on the recursive feedback
        leaves = left_tree_leaves + right_tree_leaves

    # The following lines of code return if the binary tree is full or not, depending on the number of children
    if node.left is None and node.right is None:
        is_full = 'Yes'
    if node.left is not None and node.right is not None:
        is_full = 'Yes'
    else:
        is_full = 'No'
    
    # The following lines of code use the tree's height to take an absolute value of, compare, and return the result
    is_balanced = abs(left_tree_height - right_tree_height) <= 1
    if is_balanced is True:
        is_balanced = 'Yes'
    else:
        is_balanced = 'Np'

    return height, leaves, is_full, is_balanced

'''Test Code'''
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
height, leaves, is_full, is_balanced = tree_info(root)
print(f'Height of the tree: {height}')
print(f'Number of leaf nodes: {leaves}')
print(f'is Full: {is_full}')
print(f'is Balanced: {is_balanced}')