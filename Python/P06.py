from SLL import *

class palindrome_SLL(SLL) :

    def isPalindrome(self) :
        stk = []

        self.temp = self.head

        while self.temp :
            stk.append(self.temp.data)

            self.temp = self.temp.next

        self.temp = self.head

        while self.temp :
            if stk[-1] != self.temp.data :
                return 0

            stk.pop()

            self.temp = self.temp.next

        return 1

if __name__ == '__main__':
    ll = palindrome_SLL()

    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(2)
    ll.insert(1)
    ll.insert(0)

    ll.printAll()

    if ll.isPalindrome() :
        print("\nThe Linkded list IS a Palindrome")
    else :
        print("\nThe linked list is NOT a Palindrome")