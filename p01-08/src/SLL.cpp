#include <iostream>
#include "include/SLL.h"

SLL::SLL(){
	head = NULL;
	current = NULL;
	temp = NULL;
}

void SLL::insert(int _data){
	nodePtr n = new node;
	n -> data = _data;
	n -> next = NULL;

	if(head != NULL){
		current -> next = n;

		current = current -> next;
	}else{
		head = n;
		current = head;
	}
}

void SLL::print(void){
	temp = head;
	while(temp != NULL){
		std::cout << temp->data << ", ";
		temp = temp -> next;
	}

	std::cout << std::endl;
}

int SLL::last(void){
	temp = head;
	while(temp -> next != NULL)
		temp = temp -> next;

	std::cout << "The last element is : " << temp -> data << std::endl;

	return temp -> data;
}

void SLL::lastButOne(void){
	temp = head;
	while(temp -> next -> next != NULL)
		temp = temp -> next;

	std::cout << "Last two elements are : ";

	while(temp != NULL){
		std::cout << temp -> data << ", ";
		temp = temp -> next;
	}

	std::cout << std::endl;
}

int SLL::elementAt(int index){
	temp = head;
	int count = 1;
	while(count != index){
		temp = temp -> next;
		count ++;
	}

	std::cout << "Element at index " << index<< " is : " << temp -> data << std::endl;

	return temp -> data;
}

int SLL::length(void){
	int count = 0;
	temp = head;
	while(temp != NULL){
		count++;
		temp = temp -> next;
	}

	std::cout << "No of elements in List are : " << count << std::endl;

	return count;
}

void  SLL::remove(int index){

}

void SLL::reverse(void){
	nodePtr prev = NULL;
	temp = head;
	nodePtr next = NULL;

	while(temp != NULL){
		next = temp -> next;
		temp -> next = prev;
		prev = temp;
		temp = next;
	}

	head = prev;
	current = head;

	std::cout << "The Reversed Linked List is : ";
	print();
}

void SLL::remDuplicates(void){
	temp = head;
    int cur = 0;
    std::cout << "List without duplicates is : ";
    while(temp != NULL){
        cur = temp->data;
        while(temp != NULL && cur == temp -> data){
            temp = temp -> next;
			// cur = temp -> data;
		}

        std::cout << cur << ", ";
        temp = temp -> next;
    }

	std::cout << std::endl;
}

bool SLL::isPalindrome(void){
    return 0;
}
