from SLL import *

class remDupli_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used to add functionality remove duplicates from the linked list.
    '''

    def removeDuplicates(self) :
        '''
        Removes all consicutive duplicate elements from the linked list.
        '''

        # Iterate over the linked list.
        self.temp = self.head

        while self.temp :
            cur = self.temp.data

            # Print the current element.
            print(cur, end = " ")

            # Loop till the value changes (Skip duplicates).
            while self.temp and cur == self.temp.data :
                self.temp = self.temp.next

if __name__ == '__main__':
    ll = remDupli_SLL()

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

    print("\nLinked list with removed duplicates : ")
    ll.removeDuplicates()