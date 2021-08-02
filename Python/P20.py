from SLL import *

class RemAt_SLL(SLL) :
    def removeAt(self, index) :
        prev = None

        self.temp = self.head

        count = 0

        while self.temp :
            if count == index :
                prev.next = self.temp.next
                break
            else :
                prev = self.temp

            self.temp = self.temp.next
            count += 1


if __name__ == '__main__':
    ll = RemAt_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.removeAt(3)
    print("\nLinked List after Removing element at index 3 is : ")
    ll.printAll()