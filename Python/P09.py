from SLL import *

class packDupli_SLL(SLL) :
    def packDuplicates(self) :
        self.temp = self.head

        print("(", end = "")

        while self.temp :
            cur = self.temp.data
            print("(", end = "")

            while self.temp and cur == self.temp.data :
                print(" {}".format(self.temp.data), end = "")
                self.temp = self.temp.next

            print(" )", end = "")

        print(")")

if __name__ == '__main__':
    ll = packDupli_SLL()

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
    ll.packDuplicates()