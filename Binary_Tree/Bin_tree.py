# Determine the "level" of the tree row.
# For a given tree, its "level" is given by
# 2^x < number of nodes < 2^y, where 2^x is
# the level


def get_lvl(items):
    n = 0
    while 2 ** n <= len(items):
        n += 1
    return 2 ** (n-1)


class Node:
    # Each node has a value, a left child, and a right child
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

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

        if self.order == "pre":
            self.pre_order = self.make_pre_order(self.nodes)
            print self.print_post_order(self.pre_order)
            print self.print_in_order(self.pre_order)
            print "--------------------------------------------"
        elif self.order == "post":
            self.post_order = self.make_post_order(self.nodes)
            print self.print_pre_order(self.post_order, [])
            print self.print_in_order(self.post_order, [])
            print "--------------------------------------------"
        elif self.order == "in":
            self.in_order = self.make_in_order(self.nodes)
            print self.print_pre_order(self.in_order, [])
            print self.print_post_order(self.in_order, [])
            print "--------------------------------------------"

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

    def make_post_order(self, ls):
        if len(ls) == 0:
            return None
        elif len(ls) == 1:
            return Node(ls[0])
        elif len(ls) == 3:
            node = Node(ls[2])
            node.set_left(Node(ls[0]))
            node.set_right(Node(ls[1]))

        else:
            node = Node(ls[-1])
            lvl = get_lvl(ls)
            node.set_left(self.make_post_order(ls[:lvl-1]))
            node.set_right(self.make_post_order(ls[lvl-1:-1]))
        return node

    def make_in_order(self, ls):
        if len(ls) == 0:
            return None
        elif len(ls) == 1:
            return Node(ls[0])
        elif len(ls) == 3:
            node = Node(ls[1])
            node.set_left(Node(ls[0]))
            node.set_right(Node(ls[2]))

        else:
            lvl = get_lvl(ls)
            node = Node(ls[lvl-1])
            node.set_left(self.make_in_order(ls[:lvl-1]))
            node.set_right(self.make_in_order(ls[lvl:]))
        return node

    def print_pre_order(self, cursor, result=[]):
        result.append(cursor.get_value())
        if cursor.has_left():
            self.print_pre_order(cursor.get_left(), result)
        if cursor.has_right():
            self.print_pre_order(cursor.get_right(), result)
        return result

    def print_post_order(self, cursor, result=[]):
        if cursor.has_left():
            self.print_post_order(cursor.get_left(), result)
        if cursor.has_right():
            self.print_post_order(cursor.get_right(), result)
        result.append(cursor.get_value())
        return result

    def print_in_order(self, cursor, result=[]):
        if cursor.has_left():
            self.print_in_order(cursor.get_left(), result)
        result.append(cursor.get_value())
        if cursor.has_right():
            self.print_in_order(cursor.get_right(), result)
        return result


nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pre_tree = Tree(nodes, "pre")
post_tree = Tree(nodes, "post")
in_tree = Tree(nodes, "in")

