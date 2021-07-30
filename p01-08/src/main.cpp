#include <iostream>
#include "include/SLL.h"

int main(){
	SLL list;

	list.insert(0);
	list.insert(1);
	list.insert(1);
	list.insert(1);
	list.insert(2);
	list.insert(2);

	list.insert(3);
	list.insert(3);
	list.insert(4);
	list.insert(4);
	list.insert(4);
	list.insert(4);

	std::cout << "The List is : ";
	list.print();
	list.last();
	list.lastButOne();
	list.elementAt(3);
	list.length();
	list.reverse();
	list.remDuplicates();

	// list.isPalindrome();
	return 0;
}