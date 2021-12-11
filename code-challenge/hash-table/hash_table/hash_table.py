class Node:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

        
class HashTable:

    def __init__(self, length=1024):
        self._length_of_hash_table = length
        self._hash_table = [None] * self._length_of_hash_table

    def add(self, key, value):
        """
        Takes key and value as arguements
        Hashes the key; returns hash-index
        Adds key/value pair to the HashTable at hash-index
        Handles collisions
        """
        hashed_index = self._hash(key)
        #check for collision
        if not self._hash_table[hashed_index]:
            self._hash_table[hashed_index] = Bucket()
            # add the key/value to bucket at hashed_index
        node = Node(key, value)
        self._hash_table[hashed_index].add(node)

    def get(self, key):
        """
        Takes key as arguement
        Hashes key; returns hash-index
        Returns value from table at the hash-index
        """
        key_index = self._hash(key)
        _includes_the_key = False
        if self._hash_table[key_index]:
            _includes_the_key = self._hash_table[key_index].includes(key)
        if _includes_the_key:
            return self._hash_table[key_index].return_value(key)

        

    def contains(self, key):
        """
        Takes key as arguement
        Returns boolean if key is already in HashTable
        """
        key_index = self._hash(key)
        if self._hash_table[key_index]:
            return self._hash_table[key_index].includes(key)
        return self._hash_table[key_index]

    def _hash(self, key):
        """
        Takes key as arguement
        Returns hash-index
        """
        sum_chars = 0
        for char in key: 
            sum_chars += ord(str(char))
        square_sum = sum_chars**2
        divide_square = square_sum // ord(key[0])
        return (divide_square % self._length_of_hash_table)


class Bucket:
    """Bucket used at filled index in HashTable"""

    def __init__(self):
        self.head = None

    def add(self, node):
        """Adds a node to the end of the linked list"""
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
                
            
    