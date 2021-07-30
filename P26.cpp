#include<iostream>

void combination(int*);

int main(){
    int arr[12];
    for(int i = 0; i < 12; i++)
        arr[i] = i;

    for(int i = 2; i < 9; i++){
        std::cout << "(";
        for(int j = 1; j < 10; j++){
            std::cout << "(";
            for(int k = 0; k < 11; k++){
                std::cout << "(";
                std::cout << arr[i] << ", " << arr[j] << ", " << arr[k];
                std::cout << "),";
            }
            std::cout << "),\n";
        }
        std::cout << ")\n";
    }

    return 0;
}