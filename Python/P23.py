from P03 import *
from P04 import *
from random import randint

class rndSel_SLL(eleAt_SLL, length_SLL) :

    def randomSelect(self, count) :
        l2 = eleAt_SLL()

        for i in range(count) :
            l2.insert(self.elementAt(randint(0, self.getLength()-1)))

        return l2

if __name__ == '__main__':
    ll = rndSel_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll2 = ll.randomSelect(3)
    print("Linked List of range 4 to 9 : ")
    ll2.printAll()