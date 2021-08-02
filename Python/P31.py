from math import sqrt
def isPrime(num) :
    for i in range(2, int(sqrt(num))+1) :
        if num%i == 0:
            return 0

    return 1

num = int(input("Enter the number : "))

if isPrime(num):
    print("The number is Prime")
else :
    print("The number is Not Prime")