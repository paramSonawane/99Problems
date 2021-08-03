from SLL import *

class LBO_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used to add functionality of viewing second last element in the linked list.
    '''

    def lastButOne(self):
        '''
        Helps retrive second last element of the linked list.

        Returns :
            data (int) : Data of the second last node.
        '''

        # Iterate over linked list using temp.
        self.temp = self.head

        while self.temp.next.next :
            # Advanced the temp untill it's next element points to None
            self.temp = self.temp.next

        return self.temp.data

if __name__ == "__main__" :
    ll = LBO_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    print("\nThe last-but-one element is : ", ll.lastButOne())