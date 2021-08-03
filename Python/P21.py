from SLL import *

class insrtAt_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used for adding functionality of inserting element at given index in the linked list.
    '''
    def insertAt(self, index, data) :
        '''
        Insert data in the linked list at given index.

        Parameters :
            index (int) : Index at which the element is to be inserted.
            data (Any) : Data which should be assigned to this newly inserted node.
        '''

        self.temp = self.head

        # Iterate over the linked list while keeping track of index.
        count = 0
        while self.temp :
            # If element previous to the given index is found,  add new element next to it.
            if count == index-1 :
                n = Node(data)
                n.next = self.temp.next
                self.temp.next  = n
                break

            self.temp = self.temp.next
            count += 1

if __name__ == '__main__':
    ll = insrtAt_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()
    ll.insertAt(3, 20)
    print("\nLinked List after inserting 20 at 3 : ")
    ll.printAll()