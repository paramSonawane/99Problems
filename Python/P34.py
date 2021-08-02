def gcd(a, b) :
    if(b==0) : return  a

    return gcd(b, a%b)

num = int(input("Enter the number : "))

count = 0

for i in range(1, num+1):
    if gcd(i, num) == 1 :
        count += 1

print("Euler's Totient is : ", count)