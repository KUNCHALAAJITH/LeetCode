# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # Pointer to traverse the list
        current = dummy
        
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                # Found duplicates
                val = current.next.val
                # Skip all nodes with this value
                while current.next and current.next.val == val:
                    current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        return dummy.next
