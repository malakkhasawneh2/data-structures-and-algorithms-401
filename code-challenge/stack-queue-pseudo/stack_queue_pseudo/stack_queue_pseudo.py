class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Class Stack wich implements Stack data structure with its common methods"""

    def __init__(self):

        self.top = None

    def is_empty(self):

        if self.top == None:
            return True
        return False

    def push(self, value):

        new_node = Node(value)
        new_node.next, self.top = self.top, new_node

    def pop(self):

        if not self.is_empty():
            temp, self.top = self.top, self.top.next
            temp.next = None
            return temp.value
        else:
            return ('This stack is Empty')

    def peek(self):

        if not self.is_empty():
            return self.top.value
        else:
            return ('This stack is Empty')


class PseudoQueue:
    def __init__(self, stack1):
        self.stack1 = stack1
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)
        return value

    def dequeue(self):
        """"Method to extract a value from the PseudoQueue, using a first-in, first-out approach. Returns value of extracted node """

        if self.stack1.top == None:
            raise Exception("PseudoQueue is empty")
        while self.stack1.top != None:
            stack1_item = self.stack1.pop()

            self.stack2.push(stack1_item)

        pop_val = self.stack2.pop()

        while self.stack2.top != None:
            self.stack1.push(self.stack2.pop())
        return pop_val



if __name__=="__main__":

    new_stack=PseudoQueue()

    new_stack.enqueue(4)
    new_stack.enqueue(2)
    new_stack.enqueue(3)

    print(new_stack.dequeue())
    print(new_stack.dequeue())
    print(new_stack.dequeue())




