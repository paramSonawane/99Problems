from SLL import *
from random import randint

def lottoSelect(count, limit) :
    '''
    This function is used to generate linked list with random elements.

    Inserts n random elements into the linked list with values from 0 to given limit.

    Parameters :
        count (int) : Number of elements to insert into linked list.
        limit (int) : Limit for the random value of each element.

    Returns :
        ll (SLL) : Singly linked list with random elements.
    '''

    ll = SLL()

    for i in range(count) :
        ll.insert(randint(1, limit))

    return ll

if __name__ == '__main__' :
    ll = lottoSelect(6, 49)

    print("The list after selecting 6 random elements in range [1, 49] : ")
    ll.printAll()