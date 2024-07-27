# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t=head
        l1=head
        c=1
        if head == None or head.next == None or k == 0:
            return head
        while t is not None and t.next is not None :
            c+=1
            t=t.next
        t.next=head
        k=k%c
        end=abs(c-k)
        while end:
            t=t.next
            end-=1
        head=t.next
        t.next=None
        return head
    
        # for _ in range(k-1):
        #     l1=l1.next
        
        
        