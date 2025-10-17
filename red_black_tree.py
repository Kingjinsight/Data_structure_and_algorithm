# What is it
# ==========
# A self-balancing binary search tree, each node has a color(red or black).
# The balancing rules ensure the tree remains approximately balanced.
# Guaranteeing O(log n) time complexity for insertions, deletions and searches.

# Five core rules
# ===============
# Every node is either red or black
# The root is always black
# All leaf nodes are black
# Red nodes cannot have red children
# Every path from a node to its descendant NIL nodes must have the same number of black nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1 # 1 for red, 0 for black

class RedBlackTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.rigth = None
        self.root = self.NULL
    
    def insert(self,key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        parent = None
        current = self.root

        while current!=self.NULL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right
        
        node.parent = parent
        if parent == None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node
        
        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return
        
        self._fix_insert(node)

    def _fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color =0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 0 # now k is the father node, so k.parent is the original k node
                    k.parent.parent = 1
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color == 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y 
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
