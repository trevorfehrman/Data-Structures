import math


class Heap:
    def __init__(self):
        self.storage = []

    def __repr__(self):
        return f'{self.storage}'

    def insert(self, value):
        self.storage.append(value)
        if len(self.storage) > 1:
            self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) <= 0:
            return

        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        if len(self.storage) == 2:
            snatched = self.storage.pop(0)
        elif len(self.storage) == 1:
            snatched = self.storage.pop(0)
        else:
            snatched = self.storage.pop(- 1)

        self._sift_down(0)

        return snatched

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        child_index = index
        parent_index = math.floor((child_index - 1) / 2)
        while parent_index >= 0:
            if self.storage[child_index] > self.storage[parent_index]:
                self.storage[child_index], self.storage[parent_index] = self.storage[parent_index], self.storage[child_index]
                child_index = parent_index
                parent_index = math.floor((child_index - 1) / 2)
            else:
                return

    def _sift_down(self, index):
        max_index = len(self.storage) - 1
        parent_index = index

        if len(self.storage) < 3:
            return
        print(self.storage)
        if self.storage[1] > self.storage[2]:
            child_index = 1
        else:
            child_index = 2

        while True:

            if self.storage[parent_index] < self.storage[child_index]:
                self.storage[parent_index], self.storage[child_index] = self.storage[child_index], self.storage[parent_index]

                parent_index = child_index

                if parent_index * 2 + 1 <= max_index:
                    first_child_index = parent_index * 2 + 1
                else:
                    first_child_index = max_index
                if parent_index * 2 + 2 <= max_index:
                    second_child_index = parent_index * 2 + 2
                else:
                    second_child_index = max_index

                if self.storage[first_child_index] > self.storage[second_child_index]:
                    child_index = first_child_index
                else:
                    child_index = second_child_index

            else:
                return


my_heap = Heap()

my_heap.insert(7)
my_heap.insert(12)
my_heap.insert(2)
my_heap.insert(40)
my_heap.delete()
