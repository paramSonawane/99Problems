from SLL import *

class range_SLL(SLL) :
    def initRange(self, start, end) :
        for i in range(start, end+1) :
            self.insert(i)

if __name__ == '__main__':
    ll = range_SLL()

    ll.initRange(4, 9)

    print("Linked List of range 4 to 9 : ")
    ll.printAll()