# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node_val = l1.val + l2.val 
        head_val = node_val % 10 
        carryover = 0 
        if node_val >= 10: 
            carryover = 1 

        head = ListNode(head_val)
        l1 = l1.next 
        l2 = l2.next 
        current = head

        while True: 

            #break 
            if not carryover and l1 == None and l2 == None: 
                break 
            
            if carryover and l1 == None and l2 == None: 
                current.next = ListNode(carryover)
                break 

            if l1 is None and l2 is not None: 
                number = l2.val + carryover
                if number >= 10: 
                    carryover = 1
                else: 
                    carryover = 0 
                current.next = ListNode(number%10) 
                current = current.next 
                l2 = l2.next 
            elif l1 is not None and l2 is None: 
                number = l1.val + carryover
                if number >= 10: 
                    carryover = 1
                else: 
                    carryover = 0 
                current.next = ListNode(number%10) 
                current = current.next 
                l1 = l1.next 
            else: 
                number = l1.val + l2.val + carryover
                if number >= 10: 
                    carryover = 1 
                else: 
                    carryover = 0
                current.next = ListNode(number%10) 
                current = current.next 
                l1 = l1.next
                l2 = l2.next
        return head 

            
            