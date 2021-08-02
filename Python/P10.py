from SLL import *

class RLE_SLL(SLL) :
    def RLEncode(self) :
        self.temp = self.head

        while self.temp :
            count = 0

            cur = self.temp.data

            while self.temp and cur == self.temp.data :
                count += 1
                self.temp = self.temp.next

            print("{}X{}, ".format(cur, count), end = "")

if __name__ == '__main__':
    ll = RLE_SLL()

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

    print("\nLinked list with packed duplicates : ")
    ll.RLEncode()