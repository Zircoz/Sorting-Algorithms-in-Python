class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)


def tree_sort(arr):
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    res = []
    inorder(root, res)
    return res

def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

# driver code to test the above code
arr = [1, 12, 11, 2, 13, 5, 6, 7]
print ("Given array is", end="\n")
printList(arr)
tree_sort(arr)
print("Sorted array is: ", end="\n")
printList(arr)