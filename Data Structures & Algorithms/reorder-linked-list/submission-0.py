# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find midpoint 
        fast = head 
        slow = head 
        a = head 

        while True: 

            #break 
            if fast is None or fast.next is None: 
                break 

            fast = fast.next.next
            slow = slow.next 

        #we found midpoint (slow). next, split into two linked lists, then reverse 2nd 
        b = slow.next 
        slow.next = None #this splits the list, have to do or else we get a cycle 
        prev = None 
        while b: 
            next_node = b.next 
            b.next = prev 
            prev = b 
            b = next_node 

        #merge the two halves together 
        b = prev #reset b back to prev (head of 2nd linked list. b got moved to tail when reversing )
        while b: 
            tmp1, tmp2 = a.next, b.next 
            a.next = b 
            b.next = tmp1 
            a, b = tmp1, tmp2  





