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
        leader = self.value

        if self.right == None:
            return leader

        queue = [self.right]

        while len(queue):
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if node.value > leader:
                leader = node.value
        return leader

    def for_each(self, cb):

        queue = [self]

        while len(queue):
            node = queue.pop(0)

            cb(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        return self


my_tree = BinarySearchTree(10)
my_tree.insert(3)
my_tree.insert(7)
my_tree.insert(14)
my_tree.insert(12345)


def double(num):
    print(num * 2)
    return num * 2


my_tree.for_each(double)

print(my_tree.left)


# print(my_tree)
