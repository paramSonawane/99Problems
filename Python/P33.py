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
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter Second number : "))

    # If GCD is 1 means number is co-prime.
    if gcd(num1, num2) == 1 :
        print("Given numbers ARE Co-Prime Numbers")
    else :
        print("Given Numbers are NOT Co-Prime Numbers")