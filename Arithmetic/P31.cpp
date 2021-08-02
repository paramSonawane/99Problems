#include <iostream>
#include <math.h>

bool isPrime(int);

int main(){
    int num;

    std::cout << "Enter the number : ";
    std::cin >> num;

    if(isPrime(num))
        std::cout << "The number is Prime";
    else
        std::cout << "The number is not Prime";

    return 0;
}

bool isPrime(int num){
    for(int i = 2; i <= sqrt(num); i++)
        if(num%i == 0)
            return 0;

    return 1;
}