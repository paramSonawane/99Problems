from math import sqrt

def isPrime(num) :
    '''
    Check whether given number is prime or not.

    Parameters :
        num (int) : number which is to be checked.

    Returns :
        boolean : True of number is prime else False.
    '''

    # Check if number is divisible by 0 to squar root of that number.
    for i in range(2, int(sqrt(num))+1) :
        if num%i == 0:
            return 0

    return 1

if __name__ == '__main__' :
    num = int(input("Enter the number : "))

    if isPrime(num):
        print("The number is Prime")
    else :
        print("The number is Not Prime")