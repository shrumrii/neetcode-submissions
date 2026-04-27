# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        check = self.isSameTree(root, subRoot)
        if check: 
            return True 

        if not root: 
            return False 
        
        left_check = self.isSubtree(root.left, subRoot)
        right_check = self.isSubtree(root.right, subRoot) 

        if left_check or right_check: 
            return True 
        else: 
            return False 

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #base case 
        if p is None and q is None: 
            return True 
        elif p is None and q is not None: 
            return False 
        elif p is not None and q is None: 
            return False 
        elif p.val != q.val: 
            return False 
        else:
            #recursive case 
            bool_left = self.isSameTree(p.left, q.left)
            bool_right = self.isSameTree(p.right, q.right)
            return bool_left and bool_right
