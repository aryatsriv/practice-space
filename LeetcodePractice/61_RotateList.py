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
        prev=None

        while left>0:
            prev=curr
            curr=curr.next
            left-=1


        prev.next=None
        newHead=curr
        tail.next=head


        return newHead


        
        
