class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Creates an instance of a Binary tree.
    Has a root property.
    Has three methods: pre_order, in_order, and post_order.
    """
    def __init__(self):
        self.root = None

    def pre_order(self, root=None, arr=None):
        """
        Method that takes no parameters.
        Returns an array of the values, ordered from the start, going far left, then finishing to the right.
        """
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
        """
        Method that takes no parameters.
        Returns an array of the values, ordered starting from the far left, traversing to the top, then finishing to the right.
        """
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
        """
        Method that takes no parameters.
        Returns an array of the values, ordered starting from the far left, traversing to the far right, then finishing to at the root.
        """
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

class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Method that accepts one value.
        Adds a node to the binary search tree
        Conditionals that check if the node's value is greater than or less than the "top" node
        Greater values go to the right. Lesser values go to the left.
        Continues until leaf is hit
        """
        try:
            node = _Node(value)
            if not self.root:
                self.root = node
            else:
                top = self.root
                while True:
                    if value < top.value and top.left:
                        top = top.left
                    elif value < top.value:
                        top.left = node
                        return
                    elif value > top.value and top.right:
                        top = top.right
                    else:
                        top.right = node
                        return
        except ValueError:
            return "Please enter a valid integer for the BinarySearchTree."
    
    def contains(self, value):
        """
        Method that accepts one value.
        Traverses the tree untill it reaches a node with the value that was sent in as an arguement
        Returns True or False if the value is in the tree at least once
        """
        if self.root.value != None:
            current = self.root
            if current.value == value:
                return True
            else:
                while current:
                    if current.value == value:
                        return True
                    elif value < current.value:
                        if current.left:
                            current = current.left
                            if current.value == value:
                                return True
                        else:
                            return False
                    elif value > current.value:
                        if current.right:
                            current = current.right
                            if current.value == value:
                                return True
                        else:
                            return False          
        else:
            return False
      
