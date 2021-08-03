from P03 import *
from P04 import *
from random import randint

class rndSel_SLL(eleAt_SLL, length_SLL) :
    '''
    This class is inherited from two parent classes (eleAt_SLL and length_SLL).

    This will add functionality of generating a linked list
    by randomly selecting elemnts from the original linked list.
    This class is inherited from :
        1. eleAt_SLL which has functionlity of retriving element at given index from linked list.
        2. length_SLL which has functionality of getting the length of linked list.

    Both of these classes themselves inherted from class SLL which holds basic functionlity of the linked list.

             __ eleAt_SLL <-__
            /                 \
    SLL  <-<                   >- rndSel_SLL
            \                 /
             -- length_SLL <-
    '''

    def randomSelect(self, count) :
        '''
        Select n random elements from the linked list and return a new linked list.

        Parameters :
            count (int) : Number of elements in new linked list.

        Returns :
            l2 (eleAt_SLL) : New linked list with randomly selected elements of original list.
        '''

        l2 = eleAt_SLL()

        len = self.getLength()

        # Use randint function over the range of 0 to length of linked list.
        # Select the element at randomly generated element from old linked list and insert into new.
        for i in range(count) :
            l2.insert(self.elementAt(randint(0, len - 1)))

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