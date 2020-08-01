# depth first search (DFS)
class Node:
    def __init__(self, key, left=None, right=None):
        self.val = key
        #self.children = [] # incase you want more than 2 children
        self.left = left
        self.right = right

def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val)
    printInorder(root.right)

def printPreorder(root):
    if not root:
        return
    print(root.val)
    printPreorder(root.left)
    printPreorder(root.right)

def printPostorder(root):
    if not root:
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.val)

def printInorderI(root):
    cur = root
    stack = []

    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            print(cur.val, end='-')
            cur = cur.right
    print()

def printPreorderI(root):
    cur = root
    stack = []
    while stack or cur:
        if cur:
            stack.append(cur)
            print(cur.val, end='-')
            cur = cur.left
        else:
            cur = stack.pop()
            cur = cur.right
    print()

def printPreorderII(root):
    stack = [root]
    while stack:
        item = stack.pop()
        print(item.val, end='-')
        if item.right:
            stack.append(item.right)
        if item.left:
            stack.append(item.left)
    print()

def printPostorderI(root):
    cur = root
    stack = []

    while stack or cur:
        if cur:
            if cur.right:
                stack.append(cur.right) # push in right
            stack.append(cur) # push in root
            cur = cur.left
        else:
            cur = stack.pop() 
            if cur.right and stack and cur.right == stack[-1]:
                stack.pop() # in case have right, need to handle right first
                stack.append(cur)
                cur = cur.right
            else:
                print(cur.val, end='-')
                cur = None
    print()

def printPostorderII(root):
    stack2 = []
    #preorder first
    stk =[root]
    while stk:
        item = stk.pop()
        stack2.append(item)
        if item.left:
            stk.append(item.left)
        if item.right:
            stk.append(item.right)
    stack2.reverse()
    for i in stack2:
        print (i.val, end='-')
    print()

a4 = Node(1)
a5 = Node(7)
a2 = Node(2, a4)
a6 = Node(4)
a7 = Node(6, a5)
a3 = Node(5, a6, a7)
a1 = Node(3, a2, a3)


#printInorderI(a1)
#printPreorderI(a1)
#printPreorderII(a1)
printPostorderI(a1)
printPostorderII(a1)



            
