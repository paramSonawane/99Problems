from SLL import *

class Splice_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used for adding functionality of printing slice of the linked list.
    '''

    def splice(self, start, end) :
        '''
        Prints splice of the linked list.

        Parameters :
            start (int) : Start index of the slice.
            end (int)   : End index of the slice.
        '''

        self.temp = self.head

        print("\nSplicing at indices {} & {} : ".format(start, end), end = "")

        count = 0

        # Iterate over linked list while increamenting count of index.
        while self.temp :
            #if the count is withing given bound, print it.
            if count >= start and count <= end :
                print(self.temp.data, end = ", ")

            self.temp = self.temp.next
            count += 1


if __name__ == '__main__':
    ll = Splice_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.splice(3,5)