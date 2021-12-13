# from binarytree import *
# im copy evrything in binarytree and hash table (from previos lab) and put it hear becpous the import dose not work 


# thes is the function of today lab32 : 
def tree_intersection(tree_1, tree_2):
    lst = []
    ht = HashTable()

    def recurse_traverse(node, second_tree):
        if not node:
            return
        recurse_traverse(node.left, second_tree)
        recurse_traverse(node.right, second_tree)
        if second_tree:
            if ht.contains(node.value):
                lst.append(node.value)
        else:
            ht.add(node.value)

    recurse_traverse(tree_1.root, False)
    recurse_traverse(tree_2.root, True)
    return lst

#########################################
#########################################
########## this is the code from the binarytree and hash table #############
#########################################
#########################################


class HashTable:

    def __init__(self, length=1024):
        self._length_of_hash_table = length
        self._hash_table = [None] * self._length_of_hash_table

    def add(self, key, value=None):
        hashed_index = self._hash(key)
        if not self._hash_table[hashed_index]:
            self._hash_table[hashed_index] = Bucket()

        node = Node(key, value)
        self._hash_table[hashed_index].add(node)

    def get(self, key):
        key_index = self._hash(key)
        _includes_the_key = False
        if self._hash_table[key_index]:
            _includes_the_key = self._hash_table[key_index].includes(key)
        if _includes_the_key:
            return self._hash_table[key_index].return_value(key)

        

    def contains(self, key):
        key_index = self._hash(key)
        if self._hash_table[key_index]:
            return self._hash_table[key_index].includes(key)
        return self._hash_table[key_index]

    def _hash(self, key):
        sum_chars = 0
        key = str(key)
        for char in key: 
            sum_chars += ord(str(char))
        square_sum = sum_chars**2
        divide_square = square_sum // ord(key[0])
        return (divide_square % self._length_of_hash_table)

class Node:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = _Node(value)

        if not self.root:
            self.root = node
            return
        
        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            current = q.dequeue()

            if not current.left:
                current.left = node
                return
            if not current.right:
                current.right = node
                return

            q.enqueue(current.left)
            q.enqueue(current.right)




    def pre_order(self, root=None, arr=None):
        try:
            if arr == None:
                arr = []

            arr.append(root.value)

            if root.left:
                self.pre_order(root.left, arr)

            if root.right:
                self.pre_order(root.right, arr)
            
            return arr
        except AttributeError:
            return "A root element parameter is required. Please invoke the pre_order method with a root node as an arguement."

    def post_order(self, root=None, arr=[]):
        try:
            if arr == None:
                arr = []

            if root.left:
                self.post_order(root.left, arr)
            
            if root.right:
                self.post_order(root.right, arr)
            
            arr.append(root.value)

            return arr
        except AttributeError:
            return "A root element parameter is required. Please invoke the post_order method with a root node as an arguement."

    def in_order(self, root=None, arr=[]):
        try:
            if arr == None:
                arr = []

            if root.left:
                self.in_order(root.left, arr)
            
            arr.append(root.value)
            
            if root.right:
                self.in_order(root.right, arr)
            
            return arr
        except AttributeError:
            return "A root element parameter is required. Please invoke the in_order method with a root node as an arguement."

class Queue:
    def __init__(self, front=None):
        self.front = front
        self.end = None
    
    def enqueue(self, node):
        if not self.front:
            self.front = node
        elif not self.end:
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def dequeue(self):
        try:
            first_node = self.front
            self.front = first_node.next
            first_node.next = None
            return first_node
        except AttributeError:
            return None
    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return None

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

class Bucket:
    """Bucket used at filled index in HashTable"""
    """Has Three methods: add, includes, and return_value"""
    def __init__(self):
        self.head = None

    def add(self, node):
        _next_node = None
        if not self.head:
            self.head = node
            return

        if self.head.next:    
            _next_node = self.head.next
        else:
            self.head.next = node

        while _next_node:
            if not _next_node.next:
                _next_node.next = node
                break
            _next_node = _next_node.next
    
    def includes(self, key):
        _next_node = self.head
        while _next_node:
            if _next_node.key == key:
                return True
            _next_node = _next_node.next
        return False

    def return_value(self, key):
        _current_node = self.head
        while _current_node:
            if _current_node.key == key:
                return _current_node.value
            _current_node = _current_node.next
        return None