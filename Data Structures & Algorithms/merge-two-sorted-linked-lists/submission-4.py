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

        while a and b:  
            if a.val <= b.val: 
                c.next = a 
                a = a.next 
            else: 
                c.next = b 
                b = b.next 
            c = c.next 

        if a is None and b is not None: 
            c.next = b

        if b is None and a is not None:
            c.next = a

        return dummy.next

        