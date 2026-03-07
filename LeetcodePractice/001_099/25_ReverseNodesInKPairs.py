# 25. Reverse Nodes in k-Group
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
#
#
# Follow-up: Can you solve the problem in O(1) extra memory space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head):
        prev=None      
        while head:
            next=head.next
            head.next=prev
            prev=head
            head=next
        
        return prev
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        prev=dummy
        dummy.next=head
        curr=head

        while curr:
            count=1
            start=curr
            while count<k and curr.next:
                curr=curr.next
                count+=1

            if count!=k:
                break

            next=curr.next
            curr.next=None

            newStart=self.reverseLinkedList(start)
            
            prev.next=newStart
            start.next=next
            
            curr=next
            prev=start
        
        return dummy.next
            

            
