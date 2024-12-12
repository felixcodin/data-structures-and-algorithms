//Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *pNext;
};

struct LinkedList
{
    Node *pHead;
    Node *pTail;
};

LinkedList *createLinkedList()
{
    LinkedList *ll = new LinkedList();
    if (ll != NULL)
    {
        ll->pHead = NULL;
        ll->pTail = NULL;
    }
    return ll;
}

Node *createNode(const int &value)
{
    Node *p = new Node();
    if (p != NULL)
    {
        p->data = value;
        p->pNext = NULL;
    }
    return p;
}

bool addNode(LinkedList *ll, const int &value)
{
    Node *p = createNode(value);
    if(p == NULL)
    {
        return false;
    }
    if (ll->pHead == NULL)
    {
        ll->pHead = p;
        ll->pTail = p;
        return true;
    }
    ll->pTail->pNext = p;
    ll->pTail = p;
    return true;
}

void reverse(LinkedList *ll, const int &size)
{
    if (size == 2)
    {
        int temp = ll->pHead->data;
        ll->pHead->data = ll->pTail->data;
        ll->pTail->data = temp;
        return ;
    }
    int arrTemp[size];
    Node *p = ll->pHead;
    for (int i = 0; i < size; i++)
    {
        arrTemp[size - 1 - i] = p->data;
        p = p->pNext;
    }
    p = ll->pHead;
    for (int i = 0; i < size; i++)
    {
        p->data = arrTemp[i];
        p = p->pNext;
    }
}

void displayLinkedList(LinkedList *ll)
{
    Node *p = ll->pHead;
    while (p != NULL)
    {
        cout << p->data << " ";
        p = p->pNext;
    }
    cout << endl;
}

void deleteLinkedList(LinkedList *ll)
{
    Node *p = ll->pHead;
    while (p != NULL)
    {
        ll->pHead = p->pNext;
        delete p;
        p = ll->pHead;
    }
    delete ll;
}

int main()
{
    int length;
    cout << "Enter the length (between 0 and 1000) of the list: ";
    cin >> length;

    LinkedList *ll = createLinkedList();
    for (int i = 0; i < length; i++)
    {
        int value;
        cout << "Enter " << i + 1 << "th element of list: ";
        cin >> value;
        addNode(ll, value);
    }

    cout << endl << "The initial list: ";
    displayLinkedList(ll);
    cout << endl << "The list after reversing: ";
    reverse(ll, length);
    displayLinkedList(ll);

    deleteLinkedList(ll);
    return 0;
}