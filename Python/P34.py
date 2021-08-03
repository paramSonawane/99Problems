def gcd(a, b) :
    '''
    Gives GCD of the given two number.

    Uses recursion to find the GCD of two numbers.

    Parameters :
        a (int) : First Number.
        b (int) : Second Number.

    Returns :
        Integer which is GCD of given two numbers.
    '''

    if(b==0) : return  a #Base condition
    else : return gcd(b, a%b)

if __name__ == '__main__' :
    num = int(input("Enter the number : "))

    count = 0

    # Find the Co-Prime numbers of given number and increase the count.
    for i in range(1, num+1):
        if gcd(i, num) == 1 :
            count += 1

    print("Euler's Totient is : ", count)