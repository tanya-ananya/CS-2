class TreeNode:
   def __init__(self, value, left, right):
      self.value = value
      self.left = left
      self.right = right

# Build the sample tree
grand_child1 = TreeNode(4, None, None)
grand_child2 = TreeNode(5, None, None)
child1 = TreeNode(9, grand_child1, grand_child2)
child2 = TreeNode(8, None, None)
parent = TreeNode(3, child1, child2)

# Traverse the tree - Pre order traversal (Root -> Left -> Right)
def traversePreOrder(node):
    # TODO1: implement this function
   if node is None:
      return
        # First print the data of node
   print(node.value, end=" ")
        # Then recur on left child
   traversePreOrder(node.left)
        # Finally recur on right child
   traversePreOrder(node.right)

def trim(node):
   if node is None:
      return
   node.value -= 1
   trim(node.left)
   trim(node.right)

def trim_leaves(node):
   if node is None:
      return
   if node.left is None and node.right is None:
      node.value -= 1
   else:
      trim_leaves(node.left)
      trim_leaves(node.right)
      
def mirror(node):
   if node is None:
      return 
   node.left, node.right = node.right, node.left
   mirror(node.left)
   mirror(node.right)

print()
print('Original tree:')
traversePreOrder(parent)

print('\nAfter trimming entire tree:')
trim(parent)
traversePreOrder(parent)

print('\nAfter trimming only the leaves:')
trim_leaves(parent)
traversePreOrder(parent)

print('\nAfter mirroring the tree:')
mirror(parent)
traversePreOrder(parent)
print()
print()