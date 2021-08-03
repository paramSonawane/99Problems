from SLL import *

class reverse_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used to add functionality reversing the linked list.
    '''
    
    def reverseLL(self) :
        '''
        Reverse all pointers in the linked list.
        '''

        # Maintain 3 pointers previous(prev), current(temp) and next(nxt).
        prev = None
        self.temp = self.head
        nxt = None

        # Iterate over the linked list.
        while self.temp :

            # For each iteration, point the next pointer of node to previous node.
            nxt = self.temp.next
            self.temp.next = prev
            prev = self.temp
            self.temp = nxt

        # Set the current member function as the head(which is currently last in reversed linked list).
        self.current = self.head

        # Set the head as the last pointer(Which is first in reversed linked list).
        self.head = prev

if __name__ == "__main__" :

    ll = reverse_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.reverseLL()
    print("\nThe Reversed Linked List is : ")
    ll.printAll()