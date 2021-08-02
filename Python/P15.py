from SLL import *

class repliEle_SLL(SLL) :
    def replicateEls(self, num) :
        self.temp = self.head

        while self.temp :
            i = 0
            while i < num - 1 :
                n = Node(self.temp.data)
                n.next = self.temp.next
                self.temp.next = n
                self.temp = n

                i += 1

            self.temp = self.temp.next

if __name__ == '__main__':
    ll = repliEle_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.replicateEls(3)
    print("\nLinked list after replicating elements by 3 : ")
    ll.printAll()