class Node:
 
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None


A = root = Node(1)
B = root.left = Node(2)
C = root.right = Node(3)
D = B.left = Node(4)
E = B.right = Node(5)
F = C.left = Node(6)
G = C.right = Node(7)


def depth(node):
    if not node:
        return 0
        
    left_length = depth(node.left)
    right_length = depth(node.right)

    if left_length > right_length:
        return left_length + 1
    return right_length + 1
    

print(depth(A))
