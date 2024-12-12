//Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
//An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
//Time complexity O(n + m) || Space complexity O(1)

#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isAnagram(string s, string t)
{
    if (s.length() != t.length()) //check whether the length of the two strings are equal or not.
    {
        return false;
    }
    vector<int> count(26, 0); //this will store the frequency difference of characters.
    for (int i = 0; i < s.length(); i++)
    {
        count[s[i] - 'a']++; //increment the count for character in string s
        count[t[i] - 'a']--; //decrement the count for character in string t
    }
    for (int i = 0; i < 26; i++)
    {
        if (count[i] != 0) //checks whether there is any value in the count array that is not 0 
        {
            return false;
        }
    }
    return true;
}

int main()
{
    string s;
    string t;
    cout << "Enter string s: ";
    cin >> s;
    cout << "Enter string t: ";
    cin >> t;

    //print result
    if (isAnagram(s, t))
    {
        cout << "true" << endl;
    }
    else
    {
        cout << "false" << endl;
    }

    return 0;
}