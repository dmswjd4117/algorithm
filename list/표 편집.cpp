#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#pragma warning(disable:6031)
#pragma warning(disable:6054)
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
 
using namespace std;



typedef struct _node{
    int number;
    struct _node* pre;
    struct _node* next;
    _node(int n) {
        number = n;
        pre = NULL;
        next = NULL;
    }
}Node; 

typedef struct _list {
    Node* cur;
    Node* head;
    Node* tail;
}List;

vector<Node*> removed;

void init(List* plist) {
    plist->head = new Node(-1);
    plist->tail = new Node(-1);

    plist->head->next = plist->tail;
    plist->head->pre = NULL;

    
    plist->tail->next = NULL;
    plist->tail->pre = plist->head;

    plist->cur = NULL;
}


void insert(List* plist, int number) {
    Node *newNode = new Node(number);
   

    newNode->next = plist->head->next;
    plist->head->next = newNode;

    newNode->pre = plist->head;
    newNode->next->pre = newNode;
   
    return;
}

 
void initCur(List* plist, int n) {

    plist->cur = plist->head->next;
    for (int i = 0; i < n; i++) {
        plist->cur = plist->cur->next;
    }

 
    return;
}

void printList(List list) {
 
    list.cur = list.head;
    while (list.cur->next != list.tail) {
        printf("%d ", list.cur->next->number);
        list.cur = list.cur->next;
    }
 
}

void upCur(List* plist, int n) {
 
    for (int i = 0; i < n; i++) {
        plist->cur = plist->cur->pre;
    }
 
}

void downCur(List* plist, int n) {
 

    for (int i = 0; i < n; i++) {
        plist->cur = plist->cur->next;
    }

 
    return;
}

void remove(List* plist) {
 
    if (plist->cur == NULL) {
        printf("remove error");
        exit(0);
    }

    Node* removedNode = plist->cur;

    removedNode->pre->next = removedNode->next;
    removedNode->next->pre = removedNode->pre;

    if (plist->cur->next != plist->tail) {
        plist->cur = plist->cur->next;
    }
    else {
        plist->cur = plist->cur->pre;
    }

    removed.push_back(removedNode);
}

void restore(List* plist) {
    
    if (removed.empty()) {
        printf("restore empty");
        exit(0);
    }

    Node* removedNode = removed.back();   removed.pop_back();

    removedNode->next->pre = removedNode;
    removedNode->pre->next = removedNode;

    if (plist->cur == plist->head) {
        plist->cur = removedNode;
    }
  
}

string solution(int n, int k, vector<string> cmd) {
    string answer = "";

    List list;
    init(&list);

    for (int i = n-1; i >= 0; i--) {
        insert(&list, i);
        answer += "X";
    }

    initCur(&list, k);

    for (string c : cmd) {
        // cout << "cur : " << list.cur->number << endl;

        const char op = c.at(0);
        if (op == 'U') {
            //             c.at(2) 하면 2자리 이상 수 입력일때 오류남..,,, !!
            int n = stoi(c.substr(2));
            upCur(&list, n);

            // cout << "Up " <<  n << endl;
        }
        else if (op == 'D') {
            int n = stoi(c.substr(2));
            downCur(&list, n);

            // cout << "Down " << n << endl;
        }
        else if (op == 'C') {
            // cout << "delete" << endl;
            remove(&list);
        }
        else {
            // cout << "restore" << endl;
            restore(&list);
        }
 
       
        // printList(list);
        // cout << endl;
    }

 
 
    list.cur = list.head->next;
    while (list.cur != list.tail) {
        answer[list.cur->number] = 'O';
        list.cur = list.cur->next;
    }

 
    return answer;
}


using namespace std;
 

int main(void)
{
    vector<string> cmd = { "D 2","C","U 3","C","D 4","C","U 2","Z","Z"  , "C" , "C", "C", "C", "C", "C", "C" , "Z", "Z", "D 1" , "C"};
    vector<string> cmd2 = { "D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C" };
    cout << solution(8, 2, cmd);


    return 0;
}


 