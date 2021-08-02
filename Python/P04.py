from SLL import *

class length_SLL(SLL) :
    def getLength(self) :
        self.temp = self.head

        count = 0

        while self.temp :
            self.temp = self.temp.next
            count += 1

        return count

if __name__ == "__main__" :

    ll = length_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    print("\nThe Length of Linked List is : ", ll.getLength())