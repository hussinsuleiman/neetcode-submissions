import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    
    return root

def preorder(root):
    if root is None:
        return ""
    return root.val + preorder(root.left) + preorder(root.right)

not_done = True

while not_done:
    lines = []
    
    while True:
        line = input().strip()
        
        if line == '*':
            break
        
        if line == '$':
            not_done = False
            break
        
        lines.append(line)
    
    sequence = "".join(reversed(lines))
    root = None
    
    for ch in sequence:
        root = insert(root, ch)
    
    print(preorder(root))