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
	void dropNth(int);
	void duplicateEle(void);
	int elementAt(int);
	void insert(int);
	void insertAt(int, int);
	bool isPalindrome(void);
	int last(void);
	void lastButOne(void);
	int length(void);
	void ModRLE(void);
	void print(void);
	void packDuplicates(void);
	void remDuplicates(void);
	void remove(int);
	void removeAt(int);
	void replicateEle(int);
	void reverse(void);
	void rotate(int);
	void RLEncode(void);
	void splice(int, int);
};

#endif