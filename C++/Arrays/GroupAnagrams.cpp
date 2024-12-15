//Given an array of strings 'strs', group all anagrams together into sublists. You may return the output in any order.
//An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
//Time complexity: O(m * n) || Space complexity: O(m)
//Where m is the number of strings and n is the length of longest string.

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

vector<vector<string>> groupAnagrams(vector<string> &strs)
{
    unordered_map<string, vector<string>> res; 
    for (const auto &s : strs)
    {
        vector<int> count(26, 0);   
        for (char c : s)
        {
            count[c - 'a']++; //count the number alphabetic characters present in the string.
        }
        string key = ""; //key map of string.
        for (int i = 0; i < 26; ++i) //Stores the count of each character from a-z in the string.
        {
            key += to_string(count[i]) + ',';
        }
        res[key].push_back(s); //add strings with the same key map.
    }
    vector<vector<string>> result;
    for (const auto &pair : res)
    {
        result.push_back(pair.second); //group the subsets containing anagrams into separate groups
    }
    return result;
}


int main()
{
    int size;
    cout << "Enter the size of array: ";
    cin >> size;
    vector<string> strs(size);
    vector<int> count(26, 0);
    for (int i = 0; i < size; i++)
    {
        cout << "Enter " << i + 1 << "th string of array: ";
        cin >> strs[i];
    }
    vector<vector<string>> groupedAnagrams = groupAnagrams(strs);

    //print result
    cout << "Grouped Anagrams: " << endl;
    for (const auto &group : groupedAnagrams)
    {
        for (const auto &word : group)
        {
            cout << word << " ";
        }
        cout << endl;
    }
    return 0;
}