//Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
//You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
//Return the answer with the smaller index first.
//Time complexity O(n) || Space complexity O(n)

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int main()
{
    int size;
    cout << "Enter the size of array: ";
    cin >> size;

    vector<int> nums(size);
    for (int i = 0; i < size; i++)
    {
        cout << "Enter " << i + 1 << "th element of array: ";
        cin >> nums[i];
    }

    int target;
    cout << "Enter target: ";
    cin >> target;
    
    unordered_map<int, int> mp;
    for (int i = 0; i < size; i++)
    {
        int complement = target - nums[i];
        if (mp.find(complement) != mp.end()) //checks whether the complement exists in the mp
        {
            int index1 = mp[complement];
            int index2 = i;
            if (index1 < index2) // print the smaller index first
            {
                cout << index1 << " " << index2 << endl;
            }
            else
            {
                cout << index2 << " " << index1 << endl;
            }
            break;
        }
        mp[arr[i]] = i; // store the index of the current element
    }

    return 0;
}