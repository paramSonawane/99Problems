class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class SLL :

    def __init__(self) :
        self.head = None
        self.current = None
        self.temp = None

    def insert(self, number) :
        n = Node(number)

        if self.head == None :
            self.head = n
            self.current = self.head

        else :
            self.current.next = n
            self.current = n

    def printAll(self) :
        self.temp = self.head
        while self.temp != None :
            print(self.temp.data, end = " ")
            self.temp = self.temp.next
