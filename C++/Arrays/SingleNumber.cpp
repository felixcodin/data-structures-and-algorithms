//You are given a non-empty array integers 'nums'. Every integer appears twice except for one 
//Return the integer that appears only once.
//Time complexity O(n) || Space complexity O(1)

#include <iostream>
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

    int singleNumber = 0;
    for (int num : nums)
    {
        singleNumber ^= num; //Perform XOR operation with all elements in the array.
    }
    cout << "The integer that appears only once: " << singleNumber;

    return 0;
}