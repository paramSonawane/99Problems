#include <iostream>

int gcd(int, int);

int main(){
    int num1, num2;

    std::cout << "Enter the numbers separeted by space : ";
    std::cin>> num1 >> num2;

    (gcd(num1, num2) == 1) ? std::cout << "Co-Prime Numbers" : std::cout << "Not a Co-Prime Numbers";

    return 0;
}

int gcd (int a, int b){
    return  (b == 0) ? a : gcd(b, a % b);
}