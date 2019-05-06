"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"{self.value}"

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __repr__(self):
        return f"Head: {self.head}, Tail: {self.tail} Length: {self.length}"

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        current_head = self.head

        if self.tail == None:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
            print(f"Adding {value} to head")
        else:
            self.head = ListNode(value, None, current_head)
            current_head.prev = self.head
            self.length += 1
            print(f"Adding {value} to head")

    def remove_from_head(self):
        current_head = self.head

        if current_head.next:
            self.head = current_head.next
            self.length -= 1
            print(f"Removing {current_head.value} from head")

        return current_head

    def add_to_tail(self, value):
        current_tail = self.tail

        if self.head == self.tail:
            self.tail = ListNode(value, self.head)
            self.head.next = self.tail
            self.length += 1
            print(f"Adding {value} to tail")
        else:
            self.tail = ListNode(value, current_tail)
            self.length += 1
            print(f"Adding {value} to tail")

    def remove_from_tail(self):
        current_tail = self.tail
        if self.tail == None:
            print("The list appears to be empty")

        elif self.tail == self.head:
            self.tail = None
            self.head = None
            self.length -= 1
            print(f"Removing {current_tail.value} from tail")
            return self.tail

        else:
            self.tail = current_tail.prev
            self.length -= 1
            if self.length == 1:
                self.tail = self.head
            print(f"Removing {current_tail.value} from tail")
            return current_tail

    def move_to_front(self, node):
        current_target = node
        current_head = self.head
        print(f"Moving {current_target.value} to front")
        node.delete()
        self.head.insert_before(current_target.value)
        self.head = current_target
        self.head.next = current_head

    def move_to_end(self, node):
        current_target = node
        current_tail = self.tail
        print(f"Moving {current_target.value} to tail")
        node.delete()
        self.tail.insert_after(current_target.value)
        self.tail = current_target
        self.tail.prev = current_tail
        self.tail.next = None

    def delete(self, node):
        node.delete()
        self.length -= 1

    def get_max(self):
        current = self.head
        leader = self.head.value

        while current is not self.tail:
            current = current.next
            leader = max(leader, current.value)
        print(f"Highest value is {leader}")
        return leader


my_DLL = DoublyLinkedList(ListNode("gamma"))
print(my_DLL)

my_DLL.add_to_head("beta")
print(my_DLL)
my_DLL.add_to_head("alpha")
print(my_DLL)
# my_DLL.remove_from_head()
# print(my_DLL)
# my_DLL.add_to_tail("delta")
# print(my_DLL)
# my_DLL.remove_from_tail()
# print(my_DLL)
# my_DLL.add_to_tail("New Tail")
# print(my_DLL)


print(my_DLL)
