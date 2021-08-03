from P03 import *
from P04 import *
from random import randint

class rndPrmt_SLL(eleAt_SLL, length_SLL) :
    '''
    This class is inherited from two parent classes (eleAt_SLL and length_SLL).

    This will add functionality of generating a linked list
    which is random permutation of the original linked list.
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

    def search(self, number) :
        '''
        Finds element in the linked list.

        Parameters :
            number (int) : Elements to be searched over a linked list.

        Returns :
            boolean of whether the element was found or not.
        '''

        self.temp = self.head

        # Iterate over the linked list and return 1 if the element is found.
        while self.temp :
            if self.temp.data == number :
                return 1
            else :
                self.temp = self.temp.next

        return 0

    def randomPermut(self) :
        '''
        Gives a linked list which is a random permutation of the called linked list.

        Returns :
            l2 (rndPrmt_SLL) : Linked list with random permutation.
        '''

        l2 = rndPrmt_SLL()

        len = self.getLength()

        # Iterate till length of the original linked list.
        for i in range(len) :
            # Select random element from the old linked list.
            ele = self.elementAt(randint(0, len-1))

            # Find new element which is not present in new linked list.
            while l2.search(ele) :
                ele = self.elementAt(randint(0, len-1))

            # Append this element to new linked list.
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