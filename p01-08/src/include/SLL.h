#ifndef SLL_H
#define SLL_H

class SLL{
private:
	struct node {
		int data;
		node* next;
	};

	typedef struct node* nodePtr;

	nodePtr head, current, temp;

public:
	SLL();
	int elementAt(int);
	void insert(int);
	bool isPalindrome(void);
	int last(void);
	void lastButOne(void);
	int length(void);
	void print(void);
	void remDuplicates(void);
	void remove(int);
	void reverse(void);
};

#endif