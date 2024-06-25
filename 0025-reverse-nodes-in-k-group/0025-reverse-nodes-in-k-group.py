# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            temp = head
            
           
            prevnode = None
            
            while temp is not None:
               
                front = temp.next
                
                temp.next = prevnode
               
                prevnode = temp
                
                temp = front
            return prevnode
    
        def findknode(temp, k):
            k -= 1
            while temp is not None and k > 0:
                k -= 1
                temp = temp.next
            return temp
            
        temp=head
        while temp:
            knode=findknode(temp,k)
            if knode==None:
                if prevnode:

                    prevnode.next=temp
                break
            nextnode=knode.next
            knode.next=None
            reverse(temp)
            if temp==head:
                head=knode
            else:
                prevnode.next=knode
            prevnode=temp
            temp=nextnode
        return head

        


        