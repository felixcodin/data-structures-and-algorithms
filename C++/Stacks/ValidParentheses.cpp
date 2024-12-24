/*
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
Time complexity: O(n) || Space complexity: O(n).
*/

#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>
using namespace std;


bool isValid(string s)
{
    stack<char> stack;
    unordered_map <char, char> mp = {   
        {')', '('} ,
        {']', '['} ,
        {'}', '{'}
    };

    for (char c : s) //Iterate through each character of the string 's'.
    {
        //check whether each opening bracket is closed by a closing bracket of the same type.
        if (mp.count(c))
        {
            if (!stack.empty() && stack.top() == mp[c])
            {
                stack.pop(); 
            }
            else
            {
                return false;
            }
        }
        else
        {
            stack.push(c); //store the opening brackets.
        }
    }
    return stack.empty();
}

int main()
{
    string s;
    cout << "Enter string s: ";
    cin >> s;

    if (!isValid(s))
    {
        cout << "false" << endl;
    }
    else
    {
        cout << "true" << endl;
    }

    return 0;
}