class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# node creation
first = ListNode(1)
second = ListNode(2)
third = ListNode(3)

# linking the nodes
first.next = second
second.next = third

head = curr = first
slow_pointer = fast_pointer = head

while fast_pointer and fast_pointer.next:
    slow_pointer_prev = slow_pointer
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next

middle_node = slow_pointer
print(middle_node.val)
