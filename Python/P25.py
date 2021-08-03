from P03 import *
from P04 import *
from random import randint

class rndPrmt_SLL(eleAt_SLL, length_SLL) :
    def search(self, number) :
        self.temp = self.head

        while self.temp :
            if self.temp.data == number :
                return 1
            else :
                self.temp = self.temp.next

        return 0

    def randomPermut(self) :
        l2 = rndPrmt_SLL()

        len = self.getLength()

        for i in range(len) :
            ele = self.elementAt(randint(0, len-1))
            while l2.search(ele) :
                ele = self.elementAt(randint(0, len-1))

            l2.insert(ele)

        return l2

if __name__ == '__main__':
    ll = rndPrmt_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll2 = ll.randomPermut()
    print("Linked List with random permutation : ")
    ll2.printAll()