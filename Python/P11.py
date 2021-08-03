from SLL import *

class ModRLE_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used for Modified Run-Length Encoding the linked list.
    '''

    def ModRLE(self) :
        '''
        Used to print the Modified Run-Length Encoded version of Linked List.

        The modified Run-Length encoding skips printing the frequency of the element if
        it occures only 1 time.
        
        Example :
            If the linked list is (1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5)
            It will print (1X2, 2X3, 3X4, 4, 5X3)
        '''
        self.temp = self.head

        while self.temp :
            count = 0

            cur = self.temp.data

            while self.temp and cur == self.temp.data :
                count += 1
                self.temp = self.temp.next

            if count == 1 :
                print(cur, end = ", ")
            else :
                print("{}X{}, ".format(cur, count), end = "")

if __name__ == '__main__':
    ll = ModRLE_SLL()

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

    print("\nLinked list with Modified Run-Length Encoding : ")
    ll.ModRLE()