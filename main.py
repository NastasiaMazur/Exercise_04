

# singly linked list
# node class of the singly linked list
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

    def __str__(self):
        return str(self.data)


# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the SLLNode class
        node = SLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = node
        else:  # if it is not empty, we need to find the last node and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            # set the pointer of the last node to the new node
            current.next = node
        self.size += 1  # increase the size of the list

    def get_size(self):
        return self.size

# 1

    def clear(self):
        # The method deletes all elements (nodes) in the lists. The method does not return anything.
        self.head = None
        self.size = 0

# 2

    def get_data(self, data):
        # The method searches for the given data and returns it if it is in the list or returns False otherwise.
        # It iterates through the list and checks each node's data against the given data.
        current = self.head
        while current is not None:    # loops through the list as long as it hasn't reached the end (not at a None node)
            if current.data == data:  # If the data in the current node matches the data - it returns that data.
                return data
            current = current.next    # Moves to the next node in the list.
        return False                  # Returns False if reaches the end of the list without finding a node.

# 3
    def insert(self, prev_data, data):
        node = SLLNode(data)
        current = self.head

        while current is not None and current.data != prev_data:
            # traverse the list until we find the node with value equal to prev_data or reach the end of the list.
            current = current.next

        if current is None:
            return False            # prev_data not found in the list, so we can't insert the new node.

        node.next = current.next    # sets the next pointer of the new node to the next pointer of the current node.
        current.next = node         # sets the next pointer of the current node to the new node.
        self.size += 1              # increases the size of the list.
        return True

# 4

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and not found:        # traverses the list until the end or data is found.
            if current.data == data:        #(?) would it be correct to use here 'is' instead of '==' (since we check if the current node CONTAINS the data)?
                found = True
            else:
                previous = current          # moves the previous node pointer to the current node.
                current = current.next      # moves the current node pointer to the next node.
        if current is None:                 # data not found in the list
            return
        if previous is None:
            self.head = current.next        # sets the head node to the next node.
        else:                               # data is in a non-head node.
            previous.next = current.next    # sets the previous node's next pointer to the next node.
        self.size -= 1                      # decreases the size of the list.

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value


# Usage
my_list = SinglyLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
# 1
print(my_list.get_size())
my_list.clear()                       # comment this line out to see the appended values :)
print(my_list.get_size())
# 2
print(my_list.get_data(2))
print(my_list.get_data(4))
# 3
print(my_list)
my_list.insert(2, 5)
my_list.insert(1, 7)
print(my_list)
# 4
print(f"Size before deletion: {my_list.get_size()}")
my_list.delete(2)
print(f"Size after deletion: {my_list.get_size()}")


# 5

# doubly linked list
# node class of the doubly linked list
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node
        self.prev = None  # pointer to the previous node

    def __str__(self):
        return str(self.data)


# Doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = DLLNode(data)
        if self.head is None:          # if the list is empty, the new node is both the head and the tail
            self.head = node
            self.tail = node
        else:                       # if it is not empty, set the next and prev pointers of the new node and the tail
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_node(self, index, data):
        node = DLLNode(data)
        if index == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:  # if the index is not 0, we need to find the node at the index and insert the new node after it
            current = self.head
            for i in range(index - 1):
                current = current.next
            node.prev = current
            node.next = current.next
            current.next.prev = node
            current.next = node
        self.size += 1  # increase the size of the list

    def delete(self, data):
        current = self.head
        while current is not None:  # iterate over the list
            if current.data == data:  # if we find the node to delete
                if current == self.head:  # if it is the head, set the head to the next node and set its prev pointer to None
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                elif current == self.tail:  # if it is the tail, set the tail to the previous node and set its next pointer to None
                    self.tail = current.prev
                    self.tail.next = None
                else:  # if it is not the head or tail, set the prev and next pointers of the previous and next nodes to bypass the current node
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1  # decrease the size of the list
                return  # exit the loop
            current = current.next  # move to the next node

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

# 6

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# Usage

stack = MyStack()
stack.push(11)
stack.push(22)
stack.push(33)
stack.push(44)

print(stack.size())
print(stack.top())
print(stack.pop())
print(stack.size())
print(stack.top())

# 7

class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def show_left(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def show_right(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return None

    def size(self):
        return len(self.queue)

# Usage

my_queue = MyQueue()
my_queue.push(5)
my_queue.push(6)
my_queue.push(7)
first_element = my_queue.show_left()
print(first_element)
last_element = my_queue.show_right()
print(last_element)
removed_element = my_queue.pop()
print(removed_element)
new_first_element = my_queue.show_left()
print(new_first_element)
queue_size = my_queue.size()
print(queue_size)