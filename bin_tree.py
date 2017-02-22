class Leaf():
    def __init__(self, screen, xy_pos=[0, 0], value="", radius=15, color=[0, 0, 0]):
        self.screen = screen
        self.color = color
        self.value = value
        self.radius = radius
        self.width = 1
        self.x = coord[0]
        self.y = coord[1]
        self.top_y = self.y - self.radius
        self.bot_y = self.y + self.radius
        self.left = None
        self.right = None
            
    # ----------------------SET METHODS-------------------------
    def set_color(self, color):
        self.color = color
        
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
        
    
    # ----------------------GET METHODS--------------------
    def get_value(self):
        return self.value
    
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
    
    def get_pos(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_top_y(self):
        return self.top_y


class Tree():
    root = None
    active = None
    leaf_list = []
    
    # Font info
    FONT = pyg.font.SysFont('Calibri', 22, True, False)

    def text(self, txt="", color=[0, 0, 0]):
        return self.FONT.render(txt, True, color)
    
    def __init__(self):
        pass
        
    def is_empty(self):
        return self.root is None
    
    def set_active(self, leaf):
        self.active = leaf
    
    def get_active(self):
        return self.active
        
    def get_leaf_list(self):
        return self.leaf_list
    
    def add(self, xy=[0, 0], value=""):
        # If key from numpad, ignore square brackets
        if value[0] == "[":
            value = value[1].upper()
        else:
            value = value[0].upper()
            
        # Initialize new Leaf object and append it to leaf_list
        leaf = Leaf(xy, value)
        self.leaf_list.append(leaf)
    
        # Compare x coords to determine if new leaf is 
        # the left or right child of the active leaf
        if self.active.get_x() >= leaf.get_x() and self.active.get_left() is None:
            self.active.set_left(leaf)
        elif self.active.get_right() is None:
            self.active.set_right(leaf)
            
    # Print all leaves     
    def draw(self):
        for leaf in self.leaf_list:
            pyg.draw.circle(leaf.screen, leaf.color, [leaf.x, leaf.y], leaf.radius, leaf.width)
            leaf.screen.blit(leaf.text(leaf.value, leaf.color), [leaf.x-5, leaf.y-7])
            if leaf.left is not None:
                pyg.draw.line(leaf.screen, BLACK, [leaf.left.get_x(), leaf.left.get_top_y()], [leaf.x, leaf.bot_y()], 1)
                
            if self.right is not None:
                pyg.draw.line(leaf.screen, BLACK, [leaf.right.get_x(), leaf.right.get_top_y()], [leaf.x, leaf.bot_y()], 1)

    def to_string(self, cursor=self.top, out=""):
        if not self.is_empty()
            if cursor.get_left() is not None:
                out += "("
                self.to_string(cursor.get_left(), out)
            out += cursor.get_value()
            if cursor.get_right() is not None:
                self.to_string(cursor.get_right(), out)
                out += ")"
            
            return out
