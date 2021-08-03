from SLL import *

class eleAt_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used to add functionality of viewing Kth element in the linked list.
    '''
    def elementAt(self, index) :
        '''
        Retriving element at given index as a parameter.

        Attributes :
            index (int) : Index at which the linked list data is to be retrived.

        Returns :
            data (int) : Data of the node at given index.
        '''

        self.temp = self.head

        # To keep track of index in the loop.
        count = 0

        # Iterate while the node with given index is found.
        while count != index :
            self.temp = self.temp.next
            count += 1

        # Return the data at that node.
        return self.temp.data

if __name__ == "__main__" :

    ll = eleAt_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    index = int(input("\nEnter the Index : "))

    print("\nThe Element at index {} is : {}".format(index, ll.elementAt(index)))