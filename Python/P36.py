from math import sqrt

stk = []
num = int(input("Enter the number : "))

while num%2 == 0 :
    stk.append(2)

    num /= 2

i = 3
while i <= sqrt(num) :
    while num % i == 0 :
        stk.append(i)

        num /= i

    i += 2

if num > 2 : stk.append(int(num))

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