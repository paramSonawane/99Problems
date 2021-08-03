from SLL import *

class palindrome_SLL(SLL) :
    '''
    This class is inherited from SLL class.

    It will be used to add functionality determining whether the linked list is palindrome or not.
    '''

    def isPalindrome(self) :
        '''
        Finds if the called linked list is palindrome or not.

        Returns :
            Boolean whether the linked list is palindrome or not.
        '''

        # Stack to maintain the reversed data of linked list.
        stk = []

        # Iterate over the linked list and push data of each node to stack.
        self.temp = self.head
        while self.temp :
            stk.append(self.temp.data)

            self.temp = self.temp.next

        # Iterate over the linked list again, this time check if each element match the stack.
        self.temp = self.head
        while self.temp :
            # If it doesn't match, it means the linked list is not palindrome.
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