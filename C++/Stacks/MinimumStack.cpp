/*
Design a stack class that supports the push, pop, top, and getMin operations.
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Time complexity: O(1) || Space complexity: O(n)
*/


#include <iostream>
#include <stack>
using namespace std;

class MinStack
{
    private:
        stack<int> mainStack;
        stack<int> subStack; //stack stores the minimum values at each push.
    public:
        MinStack()
        {

        }
        void push(int val)
        {
            mainStack.push(val);
            val = min(val, subStack.empty() ? val : subStack.top());
            subStack.push(val);
        }
        void pop()
        {
            mainStack.pop();
            subStack.pop();
        }
        int top()
        {
            return mainStack.top();
        }
        int getMin()
        {
            return subStack.top();
        } 
};


int main()
{
    MinStack minStack;
    minStack.push(1);
    minStack.push(2);
    minStack.push(0);   
    cout << "Minimum: " << minStack.getMin() << endl;
    minStack.pop();
    cout << "Top: " << minStack.top() << endl;
    cout << "Minimum: " << minStack.getMin() << endl;
    return 0;
}