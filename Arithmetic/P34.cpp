#include <iostream>

int gcd(int, int);

int main(){
    int num;

    std::cout << "Enter the number : ";
    std::cin >> num;

    int count = 0;

    for(int i = 1; i <= num; i++)
        if(gcd(i, num) == 1)
            count++;


    std::cout << "Euler's Totient is : " << count;
    return 0;
}

int gcd (int a, int b){
    return  (b == 0) ? a : gcd(b, a % b);
}