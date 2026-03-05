# 22. Generate Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open=0
        close=0
        res=[]
        curr=[]
        def rec(open,close):
            if open==n and close==n:
                res.append("".join(curr))
                return
            if open<n:
                curr.append('(')
                rec(open+1,close)
                curr.pop()
            if close<open:
                curr.append(')')
                rec(open,close+1)
                curr.pop()
        rec(0,0)
        return res
        
