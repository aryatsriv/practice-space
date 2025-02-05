32. Longest Valid Parentheses
Solved
Hard
Topics
Companies
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.



class Solution:
#with stack
    def longestValidParenthesesUsingStack(self, s: str) -> int:
        st=[]
        st.append(-1)
        maxLength=0

        for i,c in enumerate(s):
            if c=='(':
                st.append(i)
            else:
                st.pop()
                if len(st)==0:
                    st.append(i)
                else:
                    maxLength=max(maxLength,i-st[-1])

        return maxLength
#without stack
    def longestValidParentheses(self, s: str) -> int:
        left,right,maxLength=0,0,0

        for i in range(0,len(s)):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            if left==right:
                maxLength=max(maxLength,left+right)
            elif right>left:
                left=0
                right=0

        left=0
        right=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='(':
                left+=1
            else:
                right+=1
            if left==right:
                maxLength=max(maxLength,left+right)
            elif left>right:
                left=0
                right=0

        
        return maxLength
