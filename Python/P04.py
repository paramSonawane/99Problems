from SLL import *

class length_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used to add functionality of finding length of the linked list.
    '''

    def getLength(self) :
        '''
        Find the length of/ number of nodes in the linked list.

        Returns :
            count (int) : length of the linked list.
        '''

        self.temp = self.head

        count = 0

        # Iterate over the linked list. Keep incrementing count each iteration.
        while self.temp :
            self.temp = self.temp.next
            count += 1

        return count

if __name__ == "__main__" :

    ll = length_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    print("\nThe Length of Linked List is : ", ll.getLength())