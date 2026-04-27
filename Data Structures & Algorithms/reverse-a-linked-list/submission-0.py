# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None 
        curr = head
        while (True): 
            
            if curr == None:
                break 

            next_node = curr.next #save next node
            curr.next = prev #now set curr's next to behind me 
            prev = curr #update prev 
            curr = next_node #update curr
        return prev
