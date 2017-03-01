def get_lvl(items):
    n = 0
    while 2 ** n <= len(items):
        n += 1
    return 2 ** (n-1)


class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_parent(self, parent):
        self.parent = parent

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


class Tree:
    def __init__(self, node_list, order):
        self.nodes = node_list
        self.order = order
        self.pre_order = self.make_pre_order(self.nodes)

    def make_pre_order(self, ls):
        if len(ls) == 0:
            return None
        elif len(ls) == 1:
            return Node(ls[0])
        elif len(ls) == 3:
            node = Node(ls[0])
            node.set_left(Node(ls[1]))
            node.set_right(Node(ls[2]))

        else:
            node = Node(ls[0])
            lvl = get_lvl(ls)
            node.set_left(self.make_pre_order(ls[1:lvl]))
            node.set_right(self.make_pre_order(ls[lvl:]))
        return node

    def print_pre_order(self, cursor):
        print(cursor.get_value())
        if cursor.has_left():
            self.print_pre_order(cursor.get_left())
        if cursor.has_right():
            self.print_pre_order(cursor.get_right())

    def print_post_order(self, cursor):
        if cursor.has_left():
            self.print_post_order(cursor.get_left())
        if cursor.has_right():
            self.print_post_order(cursor.get_right())
        print(cursor.get_value())

    def print_in_order(self, cursor):
        if cursor.has_left():
            self.print_in_order(cursor.get_left())
        print(cursor.get_value())
        if cursor.has_right():
            self.print_in_order(cursor.get_right())


nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tree = Tree(nodes, "preorder")
tree.print_in_order(tree.pre_order)
