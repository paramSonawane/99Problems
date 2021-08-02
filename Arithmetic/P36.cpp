#include <iostream>
#include <math.h>

#include <stack>

int main(){
    std::stack <int> s;
    int num;

    std::cout << "Enter the number : ";
    std::cin >> num;

    for(; num % 2 == 0; s.push(2), num /= 2);

    for(int i = 3; i <= sqrt(num); i += 2)
        for(; num % i == 0; s.push(i), num /= i);

    if(num > 2) s.push(num);

    std::cout << "( ";
    int c, count;
    for(c = s.top(), count = 0; !s.empty(); s.pop()){
        if(c != s.top()){
            std::cout << "( " << c << " " << count << " ) ";
            c = s.top();
            count = 1;
        }else{
            count++;
        }
    }

    std::cout << "( " << c << " " << count << " ) )";
    return 0;
}