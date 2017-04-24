# Node class for Stack linked list
class Node:
    def __init__(self, val):
        self.value = val
        self.below = None

    def set_below(self, n):
        self.below = n

    def get_below(self):
        return self.below

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value


class Stack:  # This is a custom linked list class that acts as a stack
    header = None
    size = 0

    def __init__(self):
        pass

    # Return True if empty, False if not
    def is_empty(self):
        return self.header is None

    # Add "new" to the top of the stack
    def push(self, new):
        item = Node(new)
        if not self.is_empty():
            item.set_below(self.header)

        self.header = item
        self.size += 1

    # Return the item at the top of the stack
    def top(self):
        return self.header

    # Return the item at the top of the stack and remove it
    def pop(self):
        temp = self.top()
        self.header = self.header.get_below()
        self.size -= 1
        return temp.get_value()

    # Return the size of the stack
    def get_size(self):
        return self.size

    # Return the item just below the top item
    def second(self):
        temp = self.pop()
        sec = self.top()
        self.push(temp)

        return sec

    def to_string(self):
        print_str = ""
        for i in range(self.size):
            print_str += str(self.pop()) + ","

        return print_str[:-1]

