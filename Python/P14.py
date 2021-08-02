from SLL import *

class dupliEle_SLL(SLL) :
    def duplicateEls(self) :
        self.temp = self.head

        while self.temp :
            n = Node(self.temp.data)
            n.next = self.temp.next
            self.temp.next = n
            self.temp = n

            self.temp = self.temp.next

if __name__ == '__main__':
    ll = dupliEle_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.duplicateEls()
    print("\nLinked list after duplicating elements : ")
    ll.printAll()