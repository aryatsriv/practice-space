#25. Reverse Nodes in k-Group
#Solved
#Hard
#Topics
#Companies
#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#
#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
#You may not alter the values in the list's nodes, only nodes themselves may be changed.
#
# 
#
#Example 1:
#
#
#Input: head = [1,2,3,4,5], k = 2
#Output: [2,1,4,3,5]
#Example 2:
#
#
#Input: head = [1,2,3,4,5], k = 3
#Output: [3,2,1,4,5]
class Solution:
    def reverseLinkedList(self,head):
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

        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        curr=head

        while curr:
            start=curr
            count=1
            while count<k and curr.next:
                curr=curr.next
                count+=1

            if count!=k:
                return dummy.next
            
            prev.next=None
            next=curr.next
            curr.next=None

            newStart=self.reverseLinkedList(start)

            prev.next=newStart
            start.next=next

            prev=start
            curr=next
