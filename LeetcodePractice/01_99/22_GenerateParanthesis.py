#
#22. Generate Parentheses
#Solved
#Medium
#Topics
#Companies
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# 
#
#Example 1:
#
#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
#Example 2:
#
#Input: n = 1
#Output: ["()"]
# 
#
#Constraints:
#
#1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        curr=[]

        def rec(i,j):
            if i==n and j==n:
                res.append("".join(curr))
                return
            if i<n:
                curr.append('(')
                rec(i+1,j)
                curr.pop()
            if j<i:
                curr.append(')')
                rec(i,j+1)
                curr.pop()

        
        rec(0,0)
        return res
            
        
