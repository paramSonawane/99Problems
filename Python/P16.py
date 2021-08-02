from SLL import *

class dropNth_SLL(SLL) :
    def dropNth(self, num) :
        prev = None

        self.temp = self.head
        count = 1

        while self.temp :
            if count%num == 0 :
                prev.next = self.temp.next
                self.temp = self.temp.next
            else :
                prev = self.temp
                self.temp = self.temp.next

            count += 1


if __name__ == '__main__':
    ll = dropNth_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()
    ll.dropNth(3)

    print("\nLinked List after dropping every 3rd element : ")
    ll.printAll()