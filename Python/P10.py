from SLL import *

class RLE_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used for Run-Length Encoding the linked list.
    '''

    def RLEncode(self) :
        '''
        Used to print the Run-Length Encoded version of Linked List.

        Run-Length Encoding print the repeated consicutive elements as single element along with its frequency.

        Example :
            If the linked list is (1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5)
            It will print (1X2, 2X3, 3X4, 4X1, 5X3)
        '''

        self.temp = self.head

        # Iterate over linked list, each time keeping track of frequency of element.
        while self.temp :
            count = 0

            cur = self.temp.data

            # Keep incrementing the count till new element is found.
            while self.temp and cur == self.temp.data :
                count += 1
                self.temp = self.temp.next

            # Print the element and its count
            print("{}X{}, ".format(cur, count), end = "")

if __name__ == '__main__':
    ll = RLE_SLL()

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
    ll.RLEncode()