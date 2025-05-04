#include "happy_number.hpp"
#include <cassert>

int main()
{
    Solution sol;

    assert(sol.isHappy(1) == true);
    assert(sol.isHappy(7) == true);
    assert(sol.isHappy(19) == true);
    assert(sol.isHappy(100) == true);
    assert(sol.isHappy(2) == false);
    assert(sol.isHappy(4) == false);

    return 0;
}