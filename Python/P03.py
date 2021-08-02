from SLL import *

class eleAt_SLL(SLL) :
    def elementAt(self, index) :
        self.temp = self.head

        count = 0

        while count != index :
            self.temp = self.temp.next
            count += 1

        return self.temp.data

if __name__ == "__main__" :

    ll = eleAt_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    index = int(input("\nEnter the Index : "))

    print("\nThe Element at index {} is : {}".format(index, ll.elementAt(index)))