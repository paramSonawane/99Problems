from SLL import *

class RemAt_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used for adding functionality of removing element at given index from the linked list.
    '''

    def removeAt(self, index) :
        '''
        Removes element at passed index from the linked list.

        Parameters :
            index (int) : index of the element to be removed.
        '''

        prev = None

        self.temp = self.head

        count = 0
        # Iterate over the linked list while keeping track of index in variable count and previous node.
        while self.temp :

            # If element with given index is found, skip its address using previous node.
            if count == index :
                prev.next = self.temp.next
                break
            else :
                # Advance previous pointer.
                prev = self.temp

            # Advance the temporary pointer.
            self.temp = self.temp.next
            count += 1


if __name__ == '__main__':
    ll = RemAt_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.removeAt(3)
    print("\nLinked List after Removing element at index 3 is : ")
    ll.printAll()