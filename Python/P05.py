from SLL import *

class reverse_SLL(SLL) :
    def reverseLL(self) :
        prev = None
        self.temp = self.head
        nxt = None

        while self.temp :
            nxt = self.temp.next
            self.temp.next = prev
            prev = self.temp
            self.temp = nxt

        self.current = self.head
        self.head = prev

if __name__ == "__main__" :

    ll = reverse_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.reverseLL()
    print("\nThe Reversed Linked List is : ")
    ll.printAll()