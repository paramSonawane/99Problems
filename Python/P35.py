from math import sqrt

if __name__ == '__main__' :
    num = int(input("Enter the number : "))

    # First find all 2s
    while num%2 == 0 :
        print(2, end=" ")

        num /= 2

    # Start from 3 and check for further prime nubers
    i = 3
    while i <= sqrt(num) :
        while num % i == 0 :
            print(i, end = " ")

            num /= i

        i += 2

    # Print the factor
    num > 2 and print(int(num))
