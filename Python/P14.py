from SLL import *

class dupliEle_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used for adding functionality of duplicating each element in linked list.
    '''

    def duplicateEls(self) :
        '''
        Duplicates each element in the linked list once.
        '''

        self.temp = self.head

        # Iterate over the linked list.
        while self.temp :

            # For each iteration, add extra node after current node with same data.
            n = Node(self.temp.data)
            n.next = self.temp.next
            self.temp.next = n
            self.temp = n

            # Advance current pointer.
            self.temp = self.temp.next

if __name__ == '__main__':
    ll = dupliEle_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.duplicateEls()
    print("\nLinked list after duplicating elements : ")
    ll.printAll()