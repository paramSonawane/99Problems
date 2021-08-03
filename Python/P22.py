from SLL import *

class range_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used for adding functionality of generating linked list with items of given range.
    '''

    def initRange(self, start, end) :
        '''
        Generating the linked list with all items within given range.

        Parameters :
            start (int) : Start of range for elements.
            end (int) : End of range for elements.
        '''

        for i in range(start, end+1) :
            self.insert(i)

if __name__ == '__main__':
    ll = range_SLL()

    ll.initRange(4, 9)

    print("Linked List of range 4 to 9 : ")
    ll.printAll()