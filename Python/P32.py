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
    a = int(input("Enter first number : "))
    b = int(input("Enter Second number : "))

    print("The GCD of {} and {} is : {}".format(a, b, gcd(a, b)))