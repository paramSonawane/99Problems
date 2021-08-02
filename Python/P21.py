from SLL import *

class insrtAt_SLL(SLL) :
    def insertAt(self, index, data) :
        self.temp = self.head

        count = 0
        while self.temp :
            if count == index-1 :
                n = Node(data)
                n.next = self.temp.next
                self.temp.next  = n
                break

            self.temp = self.temp.next
            count += 1

if __name__ == '__main__':
    ll = insrtAt_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()
    ll.insertAt(3, 20)
    print("\nLinked List after inserting 20 at 3 : ")
    ll.printAll()