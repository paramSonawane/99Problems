def gcd(a, b) :
    if(b==0) : return  a

    return gcd(b, a%b)


num1 = int(input("Enter first number : "))
num2 = int(input("Enter Second number : "))

if gcd(num1, num2) == 1 :
    print("Given numbers ARE Co-Prime Numbers")
else :
    print("Given Numbers are NOT Co-Prime Numbers")