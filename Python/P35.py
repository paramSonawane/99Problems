from math import sqrt

num = int(input("Enter the number : "))

while num%2 == 0 :
    print(2, end=" ")

    num /= 2

i = 3
while i <= sqrt(num) :
    while num % i == 0 :
        print(i, end = " ")

        num /= i

    i += 2

if num > 2 : print(int(num))
