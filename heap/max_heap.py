import math


class Heap:
    def __init__(self):
        self.storage = [30, 10, 20]

    def __repr__(self):
        return f'{self.storage}'

    def insert(self, value):
        self.storage.append(value)
        if len(self.storage) > 1:
            self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        child_index = index
        parent_index = math.floor((child_index - 1) / 2)
        while parent_index >= 0:
            if self.storage[child_index] > self.storage[parent_index]:
                temp = self.storage[parent_index]
                self.storage[parent_index] = self.storage[child_index]
                self.storage[child_index] = temp
                child_index = parent_index
                parent_index = math.floor((child_index - 1) / 2)
            else:
                return

    def _sift_down(self, index):
        pass


my_heap = Heap()
# my_heap.insert(10)
# my_heap.insert(20)
# my_heap.insert(30)
my_heap.insert(40)
my_heap.insert(50)
my_heap.insert(1)
my_heap.insert(21)

print(my_heap)
