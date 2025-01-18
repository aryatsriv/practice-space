# 
# Code
# Testcase
# Testcase
# Test Result
# 148. Sort List
# Medium
# Topics
# Companies
# Given the head of a linked list, return the list after sorting it in ascending order.
# 
#  
# 
# Example 1:
# 
# 
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:
# 
# 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:
# 
# Input: head = []
# Output: []
#  
# 
# Constraints:
# 
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
#  
# 
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,head1,head2):
        if head1==None:
            return head2
        if head2==None:
            return head1
        h1curr=head1
        h2curr=head2
        dummy=TreeNode()
        curr=dummy
        while h1curr and h2curr:
            if h1curr.val<h2curr.val:
                curr.next=h1curr
                h1curr=h1curr.next
            else:
                curr.next=h2curr
                h2curr=h2curr.next
            
            curr=curr.next
        
        if h1curr:
            curr.next=h1curr
        if h2curr:
            curr.next=h2curr

        return dummy.next
  
    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        midPrev = None
        while head and head.next:
            midPrev = head if not midPrev else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid

    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

