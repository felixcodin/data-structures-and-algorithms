// Write an algorithm to determine if a number n is happy.

// A happy number is a number defined by the following process:

// Starting with any positive integer, replace the number by the sum of the squares of its digits.
// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.
#include "happy_number.hpp"
#include <unordered_set>
using namespace std;


bool Solution::isHappy(int n)
{
    unordered_set<int> hashTable;

    while (n != 1 && hashTable.find(n) == hashTable.end())
    {
        hashTable.insert(n);

        int temp = 0;
        while (n > 0)
        {
            int d = n % 10;
            temp += d * d;
            
            n /= 10;
        }
        n = temp;
    }

    if (n == 1)
    {
        return true;
    }
    return false;
}