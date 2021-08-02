#include <iostream>

int gcd(int, int);

int main(){
    std::cout << "Enter numbers separated by space : ";

    int a, b;
    std::cin >> a >>b;

    std::cout << "The GCD of " << a << " and " << b << " is : " << gcd(a,b);
    return 0;
}

int gcd (int a, int b){
    return  (b == 0) ? a : gcd(b, a % b);
}
