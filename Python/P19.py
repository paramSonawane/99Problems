from SLL import *

class rotate_SLL(SLL) :
    def rotate(self, pivot) :
        self.temp = self.head
        self.current = self.head

        i = 1
        while i < pivot :
            i += 1
            self.temp = self.temp.next

        self.head = self.temp.next
        self.temp.next = None

        self.temp = self.head
        while self.temp.next :
            self.temp = self.temp.next


        self.temp.next = self.current




if __name__ == '__main__':
    ll = rotate_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()
    ll.rotate(3)

    print("\nLinked List after rotating at 3 : ")
    ll.printAll()