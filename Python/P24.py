from SLL import *
from random import randint

def lottoSelect(count, limit) :
    ll = SLL()

    for i in range(count) :
        ll.insert(randint(1, limit))

    return ll

if __name__ == '__main__' :
    ll = lottoSelect(6, 49)

    print("The list after selecting 6 random elements in range [1, 49] : ")
    ll.printAll()