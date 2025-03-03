#65. Valid Number
#Hard
#Topics
#Companies
#Given a string s, return whether s is a valid number.
#
#For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".
#
#Formally, a valid number is defined using one of the following definitions:
#
#An integer number followed by an optional exponent.
#A decimal number followed by an optional exponent.
#An integer number is defined with an optional sign '-' or '+' followed by digits.
#
#A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
#
#Digits followed by a dot '.'.
#Digits followed by a dot '.' followed by digits.
#A dot '.' followed by digits.
#An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.
#
#The digits are defined as one or more digits.
#
# 
#
#Example 1:
#
#Input: s = "0"
#
#Output: true
#
#Example 2:
#
#Input: s = "e"
#
#Output: false
#
#Example 3:
#
#Input: s = "."
#
#Output: false
#
# 
#
#Constraints:
#
#1 <= s.length <= 20
#s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.


class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit

    def isAlphabet(self,c):
        if (ord(c)-ord('a')>=0 and ord(c)-ord('a')<26) or (ord(c)-ord('A')>=0 and ord(c)-ord('A')<26):
            return True
        return False 

    def isNumber(self,c):
        if (ord(c)-ord('0')>=0 and ord(c)-ord('a')<9):
            return True
        return False
    
    def isNumber(self, s: str) -> bool:
        
        decimalOccured=False
        eOccured=False
        isNumberStarted=False
        operaterOccured=False

        for i,c in enumerate(s):
            if self.isAlphabet(c):
                if c!='e' and c!='E':
                    return False
                elif eOccured:
                    return False
                elif i==0:
                    return False
                elif i==len(s)-1:
                    return False
                elif self.isNumber(s[i-1])==False and i-1==0:
                    return False
                elif i>=2 and self.isNumber(s[i-1])==False and self.isNumber(s[i-2])==False:
                    return False
                else:
                    eOccured=True
                    isNumberStarted=True
            elif c=='-' or c=='+':
                if i>0 and (s[i-1]=='e' or s[i-1]=='E') and i<len(s)-1 :
                    continue
                elif isNumberStarted:
                    return False
                elif operaterOccured:
                    return False
                elif i==0 and i==len(s)-1:
                    return False
                else:
                    isNumberStarted=True
                    operaterOccured=True
            elif c=='.':
                if decimalOccured or eOccured:
                    return False
                elif i==0 and i==len(s)-1:
                    return False
                if i==len(s)-1 and i>0 and (s[i-1]=='+' or s[i-1]=='-'):
                    return False
                else:
                    decimalOccured=True
                    isNumberStarted=True            
            else:
                isNumberStarted=True

        return True
