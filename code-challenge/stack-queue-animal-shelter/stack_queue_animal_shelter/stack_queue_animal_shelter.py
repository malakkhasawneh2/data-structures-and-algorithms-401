

class Node:
    """ Class for the Node instances"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """class Queue which implements Queue data structure with its common methods"""

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front == None:
            return True
        return False


    def enqueue(self, new_node):
        """Method that takes any value as an argument and adds a new node with that value to the back of the queue """

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns the node’s value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return ('This Queue is Empty')

    def peek(self):
        """Method that returns the value of the node located in the front of the queue, without removing it from the queue."""

        if not self.is_empty():
            return self.front.value
        return ('This Queue is Empty')

class Animal:
    """Class that creates animal imstance node with the given value"""
    def __init__(self, pet_name):
        self.value = pet_name
        self.next = None

class Cat(Animal):
    """Class that creates Cat node and inherits it's properties from Animal class"""
    type = 'cat'

class Dog(Animal):
    """Class that creates Dog node and inherits it's properties from Animal class"""
    type = 'dog'


class AnimalShelter:
    """Class  which holds only dogs and cats instances. The shelter operates using a first-in, first-out approach."""
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Cat) or isinstance(animal, Dog):
            self.queue1.enqueue(animal)
        else:
            return "Animal must be cat or dog"

    def dequeue(self, pref):
        adopted_animal = None

        while not self.queue1.is_empty():
            if self.queue1.front.type == pref.lower() and adopted_animal == None:
                adopted_animal= self.queue1.dequeue()
            else:
                self.queue2.enqueue(self.queue1.dequeue())

        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

        return adopted_animal



if __name__ == '__main__':

    animal_shelter = AnimalShelter()
    dog_one = Dog("Sam")
    dog_two = Dog("REX")
    dog_three = Dog("KOXE")
    animal_shelter.enqueue(dog_one)
    animal_shelter.enqueue(dog_two)
    animal_shelter.enqueue(dog_three)
    animal_shelter.dequeue("dog")
    print(animal_shelter.dog)










