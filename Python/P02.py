from SLL import *

class LBO_SLL(SLL) :
    def lastButOne(self):
        self.temp = self.head

        while self.temp.next.next :
            self.temp = self.temp.next

        return self.temp.data

if __name__ == "__main__" :
    ll = LBO_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    print("\nThe last-but-one element is : ", ll.lastButOne())