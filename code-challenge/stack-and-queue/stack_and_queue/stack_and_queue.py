class Node:
    
    """ Class for the Node instances"""
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

class Stack:
    """
    Class Stack wich implements Stack data structure with its common methods
    """        
    def __init__(self, top=None):
        self.top = top

    # def __repr__(self):
    #     return 'This is an instance of a Stack'

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            temp, self.top = self.top, self.top.next
            temp.next = None
            return temp.value
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            return None

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

class Queue:
    """
    class Queue which implements Queue data structure with its common methods
    """
    def __init__(self):
        self.front = None
        self.rear  = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            return None


    def peek(self):
        if not self.is_empty():
            return self.front.value
        return None

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

if __name__ == "__main__":
    new_stack = Stack()
    print(new_stack)