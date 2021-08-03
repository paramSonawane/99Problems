from math import sqrt

if __name__ == '__main__' :
    stk = []
    num = int(input("Enter the number : "))
    # First find all 2s
    while num%2 == 0 :
        stk.append(2)

        num /= 2

    # Start from 3 and check for further prime nubers
    i = 3
    while i <= sqrt(num) :
        while num % i == 0 :
            stk.append(i)

            num /= i

        i += 2

    # Store the factor in stk
    if num > 2 : stk.append(int(num))

    # Print it in well formated string.
    print("(", end = " ")

    c = stk[0]
    count  = 0

    for i in stk :
        if c != i :
            print("( {} {} ) ".format(c, count), end = "")
            c = i
            count = 1
        else :
            count += 1

    print("( {} {} ) )".format(c, count))