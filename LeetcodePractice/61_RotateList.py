# 61. Rotate List
# Solved
# Medium
# Topics
# Companies
# # Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# # Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head

        curr=head
        n=0
        tail=curr
        while curr:
            n+=1
            tail=curr
            curr=curr.next
        

        k=k%n
        
        if k==0:
            return head
        
        curr=head
        left=n-k
  
        while left>1:
            curr=curr.next
            left-=1

        newHead=curr.next
        curr.next=None
        
        tail.next=head


        return newHead


        
        

        
        
