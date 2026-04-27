# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        c = dummy 

        a = list1 
        b = list2 

        while True: 

            #break, both empty 
            if a is None and b is None: 
                break 

            #a empty
            if a is None and b is not None:
                c.next = b 
                break 

            #b empty 
            if a is not None and b is None:
                c.next = a 
                break 

            if a.val <= b.val:   

                c.next = a 
                a = a.next 
            else: 
                c.next = b 
                b = b.next 
            c = c.next 
    
        return dummy.next 
        

            





