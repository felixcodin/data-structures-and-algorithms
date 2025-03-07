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