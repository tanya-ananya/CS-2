#!/usr/bin/env python
# coding: utf-8

# In[8]:


# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


# Driver code
string = "{[]{()}}"
print(string,"-", check(string))

string = "[{}{})(]"
print(string,"-", check(string))

string = "((()"
print(string,"-",check(string))


# In[9]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        return ListNodeIterator(self)


class ListNodeIterator:
    def __init__(self, node):
        self.node = node

    def __next__(self):
        if self.node is not None:
            val = self.node.val
            self.node = self.node.next
            return val
        else:
            raise StopIteration

linked_list = ListNode(1, ListNode(2, ListNode(3, None)))

for n in linked_list:
    print(n)


# In[10]:


# Python Program to insert the node at the beginning of
# Linked List

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def insert_at_front(head, new_data):
  
    # Create a new node with the given data
    new_node = Node(new_data)

    # Make the next of the new node point to the current head
    new_node.next = head

    # Return the new node as the new head of the list
    return new_node


def print_list(head):
    curr = head
    while curr is not None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()


if __name__ == "__main__":
  
    # Create the linked list 2->3->4->5
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    data = 1
    head = insert_at_front(head, data)

    print_list(head)


# In[11]:


# Python Program to Insert a Node after a 
# Given Node in Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a new node after a given node
def insertAfter(head, key, newData):
    curr = head

    # Iterate over Linked List to find the key
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    # if curr becomes None means, given key is
    # not found in linked list
    if curr is None:
        return head

    # Allocate new node by given data and point
    # the next of newNode to curr's next &
    # point current next to newNode
    newNode = Node(newData)
    newNode.next = curr.next
    curr.next = newNode
    return head

def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
  
    # Create the linked list 2->3->5->6
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(6)

    key = 3
    newData = 4
    head = insertAfter(head, key, newData)

    printList(head)


# In[6]:


# Python program to delete a node from the beginning of given
# linked list
class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = None

# Function to delete the head node


def delete_head(head):
  
    # Base case if linked list is empty
    if head is None:
        return None

    # Change the head pointer to the next node
    # and free the original head
    temp = head
    head = head.next

    # Free the original head
    del temp

    # Return the new head
    return head


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print("Original list: ")
print_list(head)
# Deleting the head node
head = delete_head(head)
print("List after deleting the head: ")
print_list(head)


# In[14]:


s1 = {1,2,2,4,4,5}
s2 = {4,5,5,6}
s2.add(7) #add new item
s2.remove(6) #remove existing item
print('set 1 = ',s1)
print('set 2 =', s2)
print('union - ',s1.union(s2))
print('intersection - ',s1.intersection(s2))
print('is disjoint? - ',s1.isdisjoint(s2))
print(10 in s2) #membership test


# In[17]:


def removeDulipcates(lst):

    # convert the list into set 
    return set(lst)


# Driver Code
lst = [1, 2, 5, 1, 7, 2, 4, 2]

# Function call
print(lst)
print(removeDulipcates(lst))


# In[ ]:





# In[ ]:




