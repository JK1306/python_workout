class node:
    def __init__(self,val):
        self.right = None
        self.value = val
        self.left = None

def insert(root, node):
    if root is None:
        root = node
        return root

    if node.value < root.value:
        root.left = insert(root.left,node)

    if node.value > root.value:
        root.right = insert(root.right,node)

    return root

count = 0
def iterateBST(root):
    if root:
        iterateBST(root.left)
        iterateBST(root.right)
        print(root.value)

def findMin(root):
    if root:
        while root.left is not None:
            root = root.left
        return root

def deleteNode(root,val):
    if root.value == val:
        if root.right is not None:
            minNode = findMin(root.right)
            root.value = minNode.value
            root.left = minNode.left
            root.right = minNode.right
            minNode = None
        elif root.left is not None:
            root = 


root = node(50)
# print(root.value)
insert(root, node(10))
insert(root, node(2))
insert(root, node(80))
insert(root, node(15))
insert(root, node(60))
insert(root, node(90))
# iterateBST(root)
minVal = findMin(root)
print(minVal.value)