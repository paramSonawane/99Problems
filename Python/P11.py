from SLL import *

class ModRLE_SLL(SLL) :
    def ModRLE(self) :
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