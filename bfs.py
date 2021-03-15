# This program will return the depth and also print the nodes at each level

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

def depth(root):
    depth = 0
    q = []
    q.append(root)
    
    while q:
        depth += 1
        temp = []
        
        if not q:
            return 0
        
        for node in q:
            print(node.data, end='')
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
                
        
        q = temp
        print('\n')
    return depth


print(depth(A))
                
