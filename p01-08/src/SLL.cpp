#include <iostream>
#include <stack>
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

//P01
int SLL::last(void){
	temp = head;
	while(temp -> next != NULL)
		temp = temp -> next;

	std::cout << "The last element is : " << temp -> data << std::endl;

	return temp -> data;
}

//P02
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

//P03
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

//P04
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

//P05
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

//P06
bool SLL::isPalindrome(void){
	std::stack <int> stk;

	for(temp = head; temp != NULL; temp = temp -> next)
		stk.push(temp->data);

	for(temp = head; temp != NULL; temp = temp -> next){
		if(stk.top() != temp->data)
			return 0;
		stk.pop();
	}
    return 1;
}

//P08
void SLL::remDuplicates(void){
	temp = head;
    std::cout << "List without duplicates is : ";

    for(int cur; temp != NULL;){
        cur = temp->data;
        std::cout << cur << ", ";

		for(; temp != NULL && cur == temp -> data; temp = temp -> next);
    }

	std::cout << std::endl;
}

//P09
void SLL::packDuplicates(void){
	temp = head;
    std::cout << "Packed duplicates : (";

    for(int cur; temp != NULL;){
        cur = temp->data;
        std::cout << "(";

		for(; temp != NULL && cur == temp -> data; temp = temp -> next)
			std::cout << " " << temp -> data;

		std::cout << " )";
    }
	std::cout << ")" << std::endl;
}

//P10
void SLL::RLEncode(void){
	temp = head;
    std::cout << "Run-Length Encoding : ";

    for(int cur; temp != NULL;){
		int count = 0;
        cur = temp->data;

		for(; temp != NULL && cur == temp -> data; temp = temp -> next)
			count++;

        std::cout << count << "X" << cur << ", ";
    }

	std::cout << std::endl;
}

//P11
void SLL::ModRLE(void){
	temp = head;
    std::cout << "Modified Run-Length Encoding : ";

    for(int cur; temp != NULL;){
		int count = 0;
        cur = temp->data;

		for(; temp != NULL && cur == temp -> data; temp = temp -> next)
			count++;

		if(count == 1)
			std::cout << cur << ", ";
		else
			std::cout << count << "X" << cur << ", ";
    }

	std::cout << std::endl;
}

//P14
void SLL::duplicateEle(void){

	for(temp=head; temp!=NULL; temp = temp -> next){
		nodePtr n = new node;
		n -> data = temp -> data;
		n -> next = temp -> next;
		temp -> next = n;
		temp = n;
	}

	std::cout << "The list with duplicated elements : ";
	print();
}

//P15
void SLL::replicateEle(int num){
	for(temp=head; temp!=NULL; temp = temp -> next){
		for(int i = 0; i < num - 1; i++){
			nodePtr n = new node;
			n -> data = temp -> data;
			n -> next = temp -> next;
			temp -> next = n;
			temp = n;
		}
	}

	std::cout << "The list with replicated elements by " << num << " : ";
	print();
}

//P16
void SLL::dropNth(int num){
	nodePtr prev = NULL;

	temp = head;
	int count = 1;
	while(temp != NULL){
		if(count%num == 0){
			nodePtr dump = temp;
			prev -> next = temp -> next;
			temp = temp -> next;

			delete dump;
		}else{
			prev = temp;
			temp = temp -> next;
		}

		count++;
	}

	std::cout << "The list with every Kth element dropped : ";
	print();
}

//P18
void SLL::splice(int start, int end){
	temp = head;
	std::cout<<"Splicing at indices " << start << " & " << end <<" : ";

	for(int count = 0; temp != NULL; temp = temp -> next, count++){
		if(count >= start && count <= end)
			std::cout<< temp->data << ", ";
	}

	std::cout << std::endl;
}

//P19
void SLL::rotate(int pivot){
	temp  = head;
	current = head;

	for(int i = 1; i < pivot; i++, temp = temp -> next);

	head = temp -> next;
	temp -> next = NULL;

	for(temp = head;temp->next != NULL;temp = temp -> next);
	temp -> next = current;

	std::cout << "The rotated list is : ";
	print();
}

//P20
void SLL::removeAt(int index){
	nodePtr prev = NULL;
	temp = head;

	for(int count = 0; temp != NULL; temp = temp -> next, count++){
		if(count == index){
			prev -> next = temp -> next;

			delete temp;
			break;
		}else{
			prev = temp;
		}
	}

	std::cout << "The list after removeing element at index " << index << " : ";
	print();
}