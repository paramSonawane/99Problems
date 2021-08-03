from SLL import *

class Last_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used to add functionality of viewing last element in the linked list.
    '''

    def lastElement(self) :
        '''
        Helps retrive last element of the linked list.

        Returns :
            data (int) : Data of the second last node.
        '''

        # Iterate over the linked list using temp.
        self.temp = self.head

        while self.temp.next :
            # Advance the temp till last element is reached.
            self.temp = self.temp.next

        return self.temp.data

if __name__ == '__main__':
    ll = Last_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    print("\nThe last element is : ", ll.lastElement())