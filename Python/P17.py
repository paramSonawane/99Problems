from SLL import *

class split_SLL(SLL) :
    def split(self, index) :
        self.temp = self.head
        count = 0

        while self.temp and count < index:
            self.temp = self.temp.next
            count += 1

        l2 = SLL()

        n = self.temp.next
        self.temp.next = None

        while n :
            l2.insert(n.data)
            n = n.next

        return l2


if __name__ == '__main__':
    ll = split_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()
    ll2 = ll.split(3)

    print("\nFirst Part of Linkedlist : ")
    ll.printAll()

    print("\nLast Part of linkeed list : ")
    ll2.printAll()