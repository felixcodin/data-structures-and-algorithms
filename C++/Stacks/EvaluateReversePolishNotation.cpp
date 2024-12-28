/*
You are given an array of strings 'tokens' that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Time Complexity: O(n) || Space complexity: O(n)
*/

#include <iostream>
#include <vector>
#include <stack>
#include <string>
using namespace std;

bool isNumber(const string &str)
{
    try //check wheter string is integer or not.
    {
        stoi(str);
        return true;
    }
    catch (const invalid_argument &e)
    {
        return false;
    }
    catch (const out_of_range &e)
    {
        return false;
    }
}

int evalRPN(vector<string> &tokens)
{
    stack<int> stack;
    for (string &s : tokens)
    {
        if (isNumber(s))
        {
            stack.push(stoi(s)); //push number into stack.
        }
        else
        {
            int result = 0;
            int b = stack.top(); //pop second element.
            stack.pop();
            int a = stack.top(); //pop first element.
            stack.pop();
            if (s == "+")
            {
                result = a + b;
            }
            else if (s == "-")
            {
                result = a - b;
            }
            else if (s == "*")
            {
                result = a * b;
            }
            else if (s == "/")
            {
                result = a / b;
            }
            stack.push(result); // push result onto the top of stack to prepare for the next calculation or to conclude.
        }
    }
    return stack.top();
}

int main()
{
    vector<string> tokens;
    tokens = {"1", "2", "+", "3", "*", "4", "-"}; //test case.
    cout << evalRPN(tokens); //result: 5 is correct.

    return 0;
}