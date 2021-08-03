from SLL import *

class rotate_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used for adding functionality of rotating the linked list.
    '''

    def rotate(self, pivot) :
        '''
        Rotates the linked list at given index.

        Parameters:
            pivot (int) : Index at which the linked list will be rotated (becomes head).
        '''

        self.temp = self.head
        self.current = self.head

        # Iterate over linked list until the pivot index is found.
        i = 1
        while i < pivot :
            i += 1
            self.temp = self.temp.next

        # Assign the pivot element as new head.
        self.head = self.temp.next
        self.temp.next = None

        # Iterate over the rest of the linked list to reach the last node.
        self.temp = self.head
        while self.temp.next :
            self.temp = self.temp.next

        # Set the current as this last element for easier insertion.
        self.temp.next = self.current


if __name__ == '__main__':
    ll = rotate_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()
    ll.rotate(3)

    print("\nLinked List after rotating at 3 : ")
    ll.printAll()