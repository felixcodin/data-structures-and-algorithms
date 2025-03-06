#Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            half_pow = self.myPow(x, n // 2)
            return half_pow * half_pow
        else:
            return x * self.myPow(x, n - 1)

def test_myPow():
    solution = Solution()

    # Test case 1: Positive exponent
    assert solution.myPow(2, 10) == 1024

    # Test case 2: Negative exponent
    assert solution.myPow(2, -2) == 0.25

    # Test case 3: Exponent is zero
    assert solution.myPow(2, 0) == 1

    # Test case 4: Base is zero
    assert solution.myPow(0, 5) == 0

    # Test case 5: Base is one
    assert solution.myPow(1, 100) == 1

    # Test case 6: Base is negative, even exponent
    assert solution.myPow(-2, 4) == 16

    # Test case 7: Base is negative, odd exponent
    assert solution.myPow(-2, 3) == -8

    # Test case 8: Large exponent
    assert solution.myPow(2, 30) == 1073741824

    # Test case 9: Fractional base, positive exponent
    assert solution.myPow(0.5, 3) == 0.125

    # Test case 10: Fractional base, negative exponent
    assert solution.myPow(0.5, -2) == 4

test_myPow()
print("All test cases passed!")