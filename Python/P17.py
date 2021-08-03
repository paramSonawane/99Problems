from SLL import *

class split_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used to add functionality for spliting linked list at given index.
    '''

    def split(self, index) :
        '''
        Split the linked list at index into two seperate linked lists.

        Parameters :
            index (int) : Index at which the linked list is supposed to be splitted.

        Returns :
            l2 (SLL) : Second linked list part of the splitted linked list.
        '''

        self.temp = self.head
        count = 0

        # Iterate over the linked list until element with given index is found.
        while self.temp and count < index:
            self.temp = self.temp.next
            count += 1

        l2 = SLL()

        # Assign next element of found node to new linked list.
        n = self.temp.next

        # Break the old linked list at the index by assigning it's next to None.
        self.temp.next = None

        # Keep adding all the next elements from old linked list to new one.
        while n :
            l2.insert(n.data)
            n = n.next

        return l2


if __name__ == '__main__':
    ll = split_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()
    ll2 = ll.split(3)

    print("\nFirst Part of Linkedlist : ")
    ll.printAll()

    print("\nLast Part of linkeed list : ")
    ll2.printAll()