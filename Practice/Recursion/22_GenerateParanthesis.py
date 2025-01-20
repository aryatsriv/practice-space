# 22. Generate Parentheses
# Solved
# Medium
# Topics
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
        res=[]
        def rec(curr,openCount,closeCount):
            if openCount==n and openCount==closeCount :
                res.append("".join(curr))
            elif openCount<n:
                curr.append("(")
                rec(curr,openCount+1,closeCount)
                curr.pop()       
            if closeCount<openCount:
                curr.append(")")
                rec(curr,openCount,closeCount+1)
                curr.pop()

        rec([],0,0)
        
        return res
                            

