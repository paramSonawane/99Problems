from SLL import *

class Splice_SLL(SLL) :
    def splice(self, start, end) :
        self.temp = self.head

        print("\nSplicing at indices {} & {} : ".format(start, end), end = "")

        count = 0
        while self.temp :
            if count >= start and count <= end :
                print(self.temp.data, end = ", ")

            self.temp = self.temp.next
            count += 1


if __name__ == '__main__':
    ll = Splice_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    ll.printAll()

    ll.splice(3,5)