class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None


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
        

    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head = node
            
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
       
    def insert_before(self,data,newdata) :
        newNode = Node(newdata)
        if self.head is None:
         print("no data found")

        else:
            if self.head.data == data:
              newNode.next = self.head
              self.head = newNode

        
            if self.head.next.data == data:
                
                newNode.next = self.head.next
                self.head.next = newNode


    def insert_after(self,data,newdata) :
        node = Node(newdata)
        if self.include(data) :
            current = self.head
            while current.next != None :
                if current.data == data :
                    node.next = current.next
                    current.next = node
                    return
                current = current.next
        else :
            raise NameError("data not found")



    def kth_from_end(self, k):
            current = self.head
            list_length = 0
            while current is not None:
                current = current.next
                list_length += 1
            current = self.head

            if k > list_length:
                return ('not in the range')

            if k < 0:
                return ('negative value not allowed')


            current = self.head
            for i in range(0, list_length - k -1):
                current = current.next


            print(current.data)
            return(current.data)





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
    newlist.append(88)
    newlist.insert_before(5,200)
    newlist.insert_after(200,84)
    newlist.kthFromEnd(4)
    print(newlist.__str__())

