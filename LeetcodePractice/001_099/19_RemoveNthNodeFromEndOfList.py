# Code
#
#
# Testcase
# Testcase
# Test Result
# Debugger
# Debugger
# 19. Remove Nth Node From End of List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
# Follow up: Could you do this in one pass?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        ahead=dummy
        while n>0 and ahead:
            ahead=ahead.next
            n-=1
        
        if n>0:
            return None
        
        curr=dummy
        
        while ahead.next:
            curr=curr.next
            ahead=ahead.next
        

        curr.next=curr.next.next

        return dummy.next
