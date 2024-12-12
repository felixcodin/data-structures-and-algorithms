//Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
//Time complexity: O(n) || space complexity O(1) 

#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int size;
    cout << "Enter the size of array: ";
    cin >> size;
    map<int, int> mp;

    int *nums = new int[size];
    
    for (int i = 0; i < size; i++)
    {
        cout << "Enter " << i + 1 << "th element of array: ";
        cin >> nums[i];
        mp[nums[i]]++; //this simply stores the frequency of each element in this array.
    }

    bool isDuplicate = false;
    for (int i = 0; i < size; i++)
    {
        if (mp[nums[i]] > 1) //checks whether element frequency is more than once in this array.
        {
            isDuplicate = true;
            break;
        }
    }
    
    //print result.
    if (isDuplicate)
    {
        cout << "true" << endl;
    }
    else 
    {
        cout << "false" << endl;
    }

    delete nums;
    return 0;
}