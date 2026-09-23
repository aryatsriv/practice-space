# 22. Generate Parentheses
# Solved
# Medium
# Topics
# conpanies icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        curr=[]
        res=[]
        if n==0:
            return res
        def rec(open,closed):
            if open==n and closed==n:
                res.append(''.join(curr))
            if open<n:
                curr.append('(')
                rec(open+1,closed)
                curr.pop()
            if closed<open:
                curr.append(')')
                rec(open,closed+1)
                curr.pop()
            else:
                return
        
        rec(0,0)
        return res
        

