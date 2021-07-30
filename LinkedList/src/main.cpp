#include <iostream>
#include "include/SLL.h"

int main(){
	SLL list;

	list.insert(0);
	// list.insert(1);
	list.insert(1);
	// list.insert(1);
	// list.insert(0);
	list.insert(2);

	list.insert(3);
	// list.insert(3);
	// list.insert(4);
	// list.insert(4);
	// list.insert(4);
	list.insert(4);
	list.insert(5);
	list.insert(6);
	list.insert(7);
	list.insert(8);
	list.insert(9);


	std::cout << "The List is : ";
	list.print();

// //P01
// 	list.last();

// //P02
// 	list.lastButOne();

// //P03
// 	list.elementAt(3);

// //P04
// 	list.length();

// //P05
// 	list.reverse();

// //P06
// 	std::cout << "The list is " << (list.isPalindrome()?"a Palindrome":"not a Palindrome") << std::endl;


// //P08
// 	list.remDuplicates();

// //P09
// 	list.packDuplicates();

// //P10
// 	list.RLEncode();

// //P11
// 	list.ModRLE();

// //P14
// 	list.duplicateEle();

// //P15
// 	list.replicateEle(2);

// //P16
// 	list.dropNth(3);

// //P18
// 	list.splice(3, 7);

// //P19
// 	list.rotate(3);

// //P20
// 	list.removeAt(4);

// //P21
// 	list.insertAt(4, 4);
	return 0;
}