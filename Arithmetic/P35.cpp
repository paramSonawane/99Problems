#include <iostream>
#include <math.h>

int main(){
    int num;

    std::cout << "Enter the number : ";
    std::cin >> num;

    for(; num % 2 == 0; std::cout << 2 << " ", num /= 2);

    for(int i = 3; i <= sqrt(num); i += 2)
        for(; num % i == 0; std::cout << i << " ", num /= i);

    if(num > 2) std::cout << num;
    return 0;
}