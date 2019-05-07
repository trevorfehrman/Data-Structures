
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

import math


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if not self.head and not self.tail:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

        self.length += 1

    def remove_from_head(self):
        node = self.head

        if not self.head and not self.tail:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.head.delete()
            self.head = node.next
            self.length -= 1

        return node.value

    def add_to_tail(self, value):
        if not self.tail and not self.head:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

        self.length += 1

    def remove_from_tail(self):
        node = self.tail

        if not self.tail and not self.head:
            return node.value
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.delete()
            self.tail = node.prev

        self.length -= 1
        return node.value

    def move_to_front(self, node):
        curr = self.head

        while curr != node:
            curr = curr.next

        if curr == self.tail:
            self.tail = curr.prev
        else:
            curr.prev.next, curr.next.prev = curr.next, curr.prev

        node.next = self.head
        self.head.prev = node
        self.head = node

    def move_to_end(self, node):
        curr = self.head

        while curr != node:
            curr = curr.next

        if curr == self.head:
            self.head = curr.next
        else:
            curr.prev.next, curr.next.prev = curr.next, curr.prev

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def delete(self, node):
        curr = self.head

        if not self.head and not self.tail:
            return None
        else:
            while curr != node:
                curr = curr.next
            curr.delete()
            self.length -= 1
            if node == self.head:
                self.head = curr.next
            if node == self.tail:
                self.tail = curr.prev

    def get_max(self):
        curr = self.head
        max_val = self.head.value

        while curr != self.tail:
            curr = curr.next
            max_val = max(max_val, curr.value)

        return max_val
