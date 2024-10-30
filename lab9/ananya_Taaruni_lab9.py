class ListNode:
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next
    
def search(head, key):
    current = head
    while current is not None:
        if current.data == key:
            return True
        current = current.next
    return False
    
def insert_after_nth_node(head, n, value):
    new_node = ListNode(value)
    current = head
    count = 1
    while current is not None and count < n:
        count += 1
        current = current.next
    if current is None:
        return None
    new_node.next = current.next
    current.next = new_node

def print_linked_list(head):
  current = head
  elements = []
  while current is not None:
      elements.append(str(current.data))
      current = current.next
      print("[" + ", ".join(elements) + "]")


# Test the code
node4 = ListNode(data=4, next=None)
node2 = ListNode(data=2, next=node4)
node1 = ListNode(data=1, next=node2)
print_linked_list(node1)
insert_after_nth_node(node1, 2, 3)
print_linked_list(node1)
# Test the search function
key_to_search = 3
print(f"Is {key_to_search} in the list? {search(node1, key_to_search)}")
# key_to_search
key_not_in_list = 99
print(f"Is {key_not_in_list} in the list? {search(node1, key_not_in_list)}")