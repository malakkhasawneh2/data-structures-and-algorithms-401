class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def includes(self, data):
        current = self.head
        if current.data == data:
            return True
        else:
            while current.next != None:
                current = current.next
                if current.data == data:
                    return True
        return False
        
    def __str__(self):
        result =""
        if self.head is None:
            result += 'None'
        else:
            current = self.head
            while (current):
                result += '{ '+ f"{current.data}" + ' } -> '
                current = current.next
            result += "NULL"
            return result


if __name__ == "__main__":
    newlist = LinkedList()
    newlist.insert(5)
    newlist.insert('Hi')
    print(newlist.includes(5))
    print(newlist.includes(7))
    print(newlist.includes(7))
    print(newlist.__str__())