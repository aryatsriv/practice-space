#143. Reorder List
#Solved
#Medium
#Topics
#Companies
#You are given the head of a singly linked-list. The list can be represented as:
#
#L0 → L1 → … → Ln - 1 → Ln
#Reorder the list to be on the following form:
#
#L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
# 
#
#Example 1:
#
#
#Input: head = [1,2,3,4]
#Output: [1,4,2,3]
#Example 2:
#
#
#Input: head = [1,2,3,4,5]
#Output: [1,5,2,4,3]
# 
#
#Constraints:
#
#The number of nodes in the list is in the range [1, 5 * 104].
#1 <= Node.val <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head)->ListNode:
        if head==None:
            return None
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None:
            return 
        slow=head
        fast=head
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        prev.next=None
        if slow==fast:
            return
        reverse=self.reverseList(slow)
        i=0
        curr=dummy
        forward=head
        while forward and reverse:
            if i%2==0:
                curr.next=forward
                forward=forward.next
            else:
                curr.next=reverse
                reverse=reverse.next
            i+=1
            curr=curr.next
            curr.next=None

        if forward:
            curr.next=forward
        if reverse:
            curr.next=reverse

        return dummy.next


            
        
        
