class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        root = Node(data)
        self.root = root

    def insert_left(self, node, data):
        left = Node(data)
        node.left = left

    def insert_right(self, node, data):
        right = Node(data)
        node.right = right

    def __str__(self):
        st = ""

        def rec_str(n):
            nonlocal st
            if n is None:
                st += "_"
            else:
                st += str(n.data)
                st += "("
                rec_str(n.left)
                st += ","
                rec_str(n.right)
                st += ")"
        rec_str(self.root)
        return st


t = Tree()
t.insert_root("A")
t.insert_left(t.root, "B")
t.insert_right(t.root, "C")
t.insert_left(t.root.left, "D")
t.insert_right(t.root.left, "E")
t.insert_right(t.root.right, "F")
print(t)


class BinarySearchTree(Tree):
    def __init__(self):
        super().__init__()

    def insert(self, data):
        if self.root is None:
            self.insert_root(data)
            return
        start = self.root
        while True:
            if data == start.data:
                print(str(data)+" is already in the tree.")
                break
            elif data < start.data:
                if start.left is None:
                    start.left = Node(data)
                    break
                else:
                    start = start.left
                    continue
            else:
                if start.right is None:
                    start.right = Node(data)
                    break
                else:
                    start = start.right
                    continue

    def inorder(self):
        result = []

        def rec_inorder(n):
            nonlocal result
            if n is not None:
                rec_inorder(n.left)
                result.append(n.data)
                rec_inorder(n.right)
        rec_inorder(self.root)
        return result



b = BinarySearchTree()
b.insert(5)
print(b)
b.insert(3)
print(b)
b.insert(2)
print(b)
b.insert(4)
print(b)
b.insert(10)
print(b)
b.insert(10)
print(b)
b.insert(7)
b.insert(11)
b.insert(14)
print(b)
print(b.inorder())















