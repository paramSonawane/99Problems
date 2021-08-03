from SLL import *

class packDupli_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used to add functionality packing the duplicates with round brackets in linked list.
    '''

    def packDuplicates(self) :
        '''
        Prints packed version of data nodes with duplicates in round brackets in the linked list.
        '''

        self.temp = self.head

        print("(", end = "")

        # Iterate over linked list untill temp is None.
        while self.temp :
            cur = self.temp.data
            print("(", end = "")

            # Each time print the element with preciding round bracket.
            while self.temp and cur == self.temp.data :
                print(" {}".format(self.temp.data), end = "")
                self.temp = self.temp.next

            # End the loop with closing round bracket.
            print(" )", end = "")

        print(")")

if __name__ == '__main__':
    ll = packDupli_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(1)
    ll.insert(3)
    ll.insert(4)
    ll.insert(4)
    ll.insert(5)
    ll.insert(5)
    ll.insert(5)
    ll.insert(6)

    ll.printAll()

    print("\nLinked list with packed duplicates : ")
    ll.packDuplicates()