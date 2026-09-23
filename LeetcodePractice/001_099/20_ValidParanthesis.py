# 20. Valid Parentheses
# Solved
# Easy
# Topics
# conpanies icon
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        cache=deque()
        open=set(['(','[','{'])
        close_open={')':'(',']':'[','}':'{'}
        for c in s:
            if c in open:
                cache.append(c)
            elif c in close_open and len(cache)>0:
                val=cache.pop()
                if val!=close_open[c]:
                    return False
            else:
                return False
        

        return True if len(cache)==0 else False
                
            