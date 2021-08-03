from SLL import *

class repliEle_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used for adding functionality of replicating each element n times in linked list.
    '''

    def replicateEls(self, num) :
        '''
        Replicates each element in the linked list num times.

        Parameters :
            num (int) : Number of time each element to be replicated.
        '''
        self.temp = self.head

        # Iterate over the linked list.
        while self.temp :
            i = 0
            # For each iteration, add extra (num) nodes after current node with same data.
            while i < num - 1 :
                n = Node(self.temp.data)
                n.next = self.temp.next
                self.temp.next = n
                self.temp = n

                i += 1


            # Advance the iteration pointer.
            self.temp = self.temp.next

if __name__ == '__main__':
    ll = repliEle_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.replicateEls(3)
    print("\nLinked list after replicating elements by 3 : ")
    ll.printAll()