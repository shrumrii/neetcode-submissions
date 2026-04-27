# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head) #dummy.next = head 
        first = dummy
        second = dummy 

        for _ in range(n+1): 
            first = first.next 

        while first: 
            first = first.next
            second = second.next 

        second.next = second.next.next 

        return dummy.next

        # if head.next == None: 
        #     return None 

        # first = head
        # second = head 
        # head_start = n 
        # prev = None 

        # while True: 

        #     #break 
        #     if first == None: 
        #         break 

        #     if head_start > 0: 
        #         first = first.next
        #         head_start -= 1 
        #     else:
        #         first = first.next 

        #         prev = second 
        #         second = second.next 
        
        # if prev == None: 
        #     return head.next
        # else: 
        #     prev.next = second.next 
        # return head
                
        



        
        
        

