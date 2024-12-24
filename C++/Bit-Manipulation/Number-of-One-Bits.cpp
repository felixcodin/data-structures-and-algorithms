//You are given an unsigned integer n. Return the number of 1 bits in its binary representation.
//You may assume n is a non-negative integer which fits within 32-bits.
//Time complexity O(1) || Space comlexity O(1)

#include <iostream>
#include <cstdint>
using namespace std;

int countBitOne(uint32_t x)
{
    int count = 0;
    for (int i = 0; i < 32; i++)
    {
        if ((1 << i) & x) //this simply counts the number of 1 bits in the 'n' by shifting the bit 1 i times.
        {
            count++;
        }
    }
    return count;
}

int main()
{
    uint32_t n;
    cout << "Enter an unsigned integer n: ";
    cin >> n;
    int quantityBitOne = countBitOne(n);
    cout << "Quantity of bit one in n: " << quantityBitOne << endl;
    return 0;
}