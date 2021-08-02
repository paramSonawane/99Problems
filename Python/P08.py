from SLL import *

class remDupli_SLL(SLL) :
    def removeDuplicates(self) :
        self.temp = self.head

        while self.temp :
            cur = self.temp.data
            print(cur, end = " ")

            while self.temp and cur == self.temp.data :
                self.temp = self.temp.next

if __name__ == '__main__':
    ll = remDupli_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(1)
    ll.insert(3)
    ll.insert(4)
    ll.insert(4)
    ll.insert(5)
    ll.insert(5)
    ll.insert(5)
    ll.insert(6)

    ll.printAll()

    print("\nLinked list with removed duplicates : ")
    ll.removeDuplicates()