//Given an array 'nums' and an integer 'k', return the 'k' most frequent elements within the array.
//The test cases are generated such that the answer is always *unique*
//Time complexity: O(n) || Space complexity: O(n)

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> topKFrequent(vector<int> &nums, const int &k)
{
    unordered_map<int, int> count;
    vector<vector<int>> freq(nums.size() + 1);
    
    for (int n : nums)
    {
        count[n]++; //store the frequency of each number in 'nums'
    }
    for (const auto &pair : count)
    {
        freq[pair.second].push_back(pair.first); //for each frequency, store the number into 'freq'
    }
    vector<int> result;
    for (int i = freq.size() - 1; i > 0; i--)
    {
        for (int n : freq[i])
        {
            result.push_back(n);
            if (result.size() == k) //this ensures that we only collect the exact k most frequent elements.
            {
                return result;
            }
        }
    }
    return result;
}

int main()
{
    vector<int> nums;
    
    //test case.
    nums = {1, 2, 2, 3, 3, 3};
    int k = 2;

    nums = topKFrequent(nums, k);
    cout << "Top " << k << " frequent element: ";
    for (int i = 0; i < size(nums); i++)
    {
        cout << nums[i] << " ";
    }
    return 0;
}