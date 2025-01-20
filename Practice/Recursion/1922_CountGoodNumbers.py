# 1922. Count Good Numbers
# Attempted
# Medium
# Topics
# Companies
# Hint
# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
# 
# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.
# 
# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
# 
#  
# 
# Example 1:
# 
# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
# Example 2:
# 
# Input: n = 4
# Output: 400
# Example 3:
# 
# Input: n = 50
# Output: 564908303
#  
# 
# Constraints:
# 
# 1 <= n <= 1015
class Solution:
    def myPow(self, x: float, n: int) -> float:
        mod = 1000000007
        if n==0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        
        if n%2==0:
            return self.myPow((x*x)%mod, n//2)
        else:
            return x * self.myPow((x*x)%mod, (n-1)//2)

    def countGoodNumbers(self, n: int) -> int:
        if n==1:
            return 5

        odd=n//2
        even=n-odd

        count= self.myPow(4,odd)% (10**9+7)
        count*=self.myPow(5,even)%(10**9+7)

        return count%(10**9+7)