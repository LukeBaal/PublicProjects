class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nxt = None
        self.prev = None

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_nxt(self, item):
        self.nxt = item

    def get_next(self):
        return self.nxt

    def set_prev(self, item):
        self.prev = item

    def get_prev(self):
        return self.prev


class LinkedList:
    header = None
    tail = None
    size = 0

    def __init__(self):
        pass

    # Determine whether the list is empty or not
    def is_empty(self):
        return self.header is None

    # Append an item to the end of the list
    def append(self, item):
        if self.is_empty():
            self.header = item

        if self.tail is not None:
            self.tail.set_nxt(item)
            item.set_prev(self.tail)

        self.tail = item
        self.size += 1

    # Return the head of the list
    def get_head(self):
        return self.header

    # Return the tail of the list
    def get_tail(self):
        return self.tail

    # Return the item at the specified index
    def get(self, index):
        cursor = self.header
        for i in range(index):
            if i <= self.size:
                cursor = cursor.get_next()
        return cursor

    # Change the value of the item at the given index
    def set(self, item, index):
        cursor = self.header
        for i in range(index - 1):
            if i <= self.size:
                cursor = cursor.get_next()
        cursor.set_xy(item.x, item.y)

    # Remove the item at the given index
    def remove(self, index):
        cursor = self.header
        for i in range(index - 1):
            if i <= self.size:
                cursor.get_next()
        if cursor == self.tail:
            self.tail = cursor.prev
            self.tail.set_nxt(None)

        if cursor == self.header:
            self.header = cursor.nxt
            self.header.set_prev(None)

        cursor.prev.set_nxt(cursor.nxt)
        cursor.nxt.set_prev(cursor.prev)
        self.size -= 1

    # Return the size of the list
    def get_size(self):
        return self.size

    # Assume index1 < index2
    def swap(self, index1, index2):
        temp_prev = index1.get_prev()
        # index1 and index2 are next to each other
        if index1.get_next() == index2:
            if index1.get_prev() is not None:
                index1.get_prev().set_nxt(index2)
            if index1 == self.header:
                self.header = index2
            index1.set_prev(index2)
            index1.set_nxt(index2.get_next())

            if index2.get_next() is not None:
                index2.get_next().set_prev(index1)
            if index2 == self.tail:
                self.tail = index1
            index2.set_prev(temp_prev)
            index2.set_nxt(index1)

        # Index1 and Index2 are NOT next to each other
        else:
            temp_next = index1.get_next()

            if index1.get_prev() is not None:
                index1.get_prev().set_nxt(index2)
            if index1.get_next() is not None:
                index1.get_next().set_prev(index2)
            if index1 == self.header:
                self.header = index2
            index1.set_prev(index2.get_prev())
            index1.set_nxt(index2.get_next())

            if index2.get_prev() is not None:
                index2.get_prev().set_nxt(index1)
            if index2.get_next() is not None:
                index2.get_next().set_prev(index1)
            if index2 == self.tail:
                self.tail = index1
            index2.set_prev(temp_prev)
            index2.set_nxt(temp_next)

    # Return the list as a string
    def to_string(self):
        print_str = "[" + str(self.header.to_string()) + ', '
        cursor = self.header
        while cursor.nxt is not None:
            cursor = cursor.nxt
            print_str += str(cursor.to_string()) + ', '

        print_str = print_str[:len(print_str)-2] + ']'
        return print_str

    # Return the x or y coords as a string, depending on the given string
    def get_coords(self, n):
        x_coords = str(self.header.get_x()) + ","
        y_coords = str(self.header.get_y()) + ","
        cursor = self.header
        while cursor.get_next() is not None:
            cursor = cursor.get_next()
            x_coords += str(cursor.get_x()) + ","
            y_coords += str(cursor.get_y()) + ","

        x_coords = x_coords[:len(x_coords)-2]
        y_coords = y_coords[:len(y_coords) - 2]

        if n == "x":
            return x_coords
        elif n == "y":
            return y_coords
