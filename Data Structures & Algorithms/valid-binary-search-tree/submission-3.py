# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        lo = float('-inf')
        hi = float('inf') 

        def validate(node, lo, hi): 

            #base case 
            if node == None: 
                return True 

            if not (lo < node.val < hi):
                return False 

            return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)
        return validate(root, lo, hi)
         
            

        

        
