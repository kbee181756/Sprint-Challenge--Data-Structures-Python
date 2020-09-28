class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                new_node = BSTNode(value)
                self.right = new_node
        else:
            if self.left:
                self.left.insert(value)
            else:
                new_node = BSTNode(value)
                self.left = new_node
    
    def contains(self, point):
        if self.value == point:
            return True
        elif point > self.value:
            if self.right:
                return self.right.contains(point)
            else:
                return False
        else:
            return self.left.contains(point) if self.left else False
    
    def get_max(self):
        max = self.value
        if self.right:
            return self.right.get_max()
        else:
            return max

    def every_one(self, fn):
        fn(self.value)
        if self.right:
            self.right.every_one(fn)
        if self.left:
            self.left.every_one(fn)