class Node :
    '''
    This class is basic block in the linked list.

    Attributes:
        data (Any)  : Storing data part of node.
        next (Node) : Storing reference to next node.
    '''

    def __init__(self, data) :
        '''
        Costructor can be used directly to initialize a node with some data.

        Parameters:
            data (Any) : Data which is to be stored in the node.
        '''

        self.data = data
        self.next = None

class SLL :
    '''
    This class contains all basic operations on linked list.

    For all further examples (1 - 23) this class will be extended in respective files.

    Attributes:
        head    (Node) : Stores start of linked list.
        current (Node) : Stores last node added to linked list for easier insertion.
        temp    (Node) : Temporary Reference can be used for other logics.
    '''

    def __init__(self) :
        '''
        Costructor sets all the class members to None.
        '''

        self.head = None
        self.current = None
        self.temp = None

    def insert(self, number) :
        '''
        Inserts new node to the linked list.

        Parameters:
            number (int) : Number to append to the linked list.
        '''

        # Create node with given paramater as value.
        n = Node(number)

        # For inserting for the first time, set head node and current node to new node.
        if self.head == None :
            self.head = n
            self.current = self.head

        # Otherwise assign new node to current node's next.
        else :
            self.current.next = n
            self.current = n

    def printAll(self) :
        '''
        Function to print all the data currently in the linked list.
        '''

        # Set temporary variable at the start of linked list.
        self.temp = self.head

        # Iterate over the linked list till end.
        while self.temp != None :
            # For each iteration print the data in the node.

            print(self.temp.data, end = " ")
            self.temp = self.temp.next
