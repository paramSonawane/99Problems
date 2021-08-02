def gcd(a, b) :
    if(b==0) : return  a
    else : return gcd(b, a%b)

a = int(input("Enter first number : "))
b = int(input("Enter Second number : "))

print("The GCD of {} and {} is : {}".format(a, b, gcd(a, b)))