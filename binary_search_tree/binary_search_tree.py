class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Value: {self.value} Left: {self.left} Right: {self.right}"

    def insert(self, value):
        node = BinarySearchTree(value)

        current = self
        while True:
            if node.value < current.value:
                if current.left == None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                if current.right == None:
                    current.right = node
                    return
                else:
                    current = current.right

    def contains(self, target):
        current = self

        while True:
            if target == current.value:
                return True
            elif current.left == None and current.right == None:
                return False
            elif target < current.value:
                current = current.left
            else:
                current = current.right

    def get_max(self):
        pass

    def for_each(self, cb):
        pass


my_tree = BinarySearchTree(10)
my_tree.insert(3)
my_tree.insert(7)
my_tree.insert(14)
my_tree.insert(12345)

print(my_tree.contains(12346))


# print(my_tree)
