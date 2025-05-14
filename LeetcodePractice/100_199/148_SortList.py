#148. Sort List
#Medium
#Topics
#Companies
#Given the head of a linked list, return the list after sorting it in ascending order.
#
# 
#
#Example 1:
#
#
#Input: head = [4,2,1,3]
#Output: [1,2,3,4]
#Example 2:
#
#
#Input: head = [-1,5,3,4,0]
#Output: [-1,0,3,4,5]
#Example 3:
#
#Input: head = []
#Output: []
# 
#
#Constraints:
#
#The number of nodes in the list is in the range [0, 5 * 104].
#-105 <= Node.val <= 105
# 
#
#Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,left,right):
        dummy=ListNode()
        newList=dummy
        while left and right:
            if left.val<right.val:
                newList.next=left
                left=left.next
            else:
                newList.next=right
                right=right.next
            newList=newList.next
        
        if left:
            newList.next=left
        if right:
            newList.next=right

        return dummy.next

       
    def getMid(self, head):
        if head==None or head.next==None:
            return None
        fast=head
        slow=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        
        prev.next=None
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        mid=self.getMid(head)
        left=self.sortList(head)
        right=self.sortList(mid)
        return self.merge(left,right)
        
