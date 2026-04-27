# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #base case 
        if root == None: 
            return root; 

        #recursive case 
        revRootLeft = self.invertTree(root.left) 
        revRootRight = self.invertTree(root.right)

        root.left = revRootRight
        root.right = revRootLeft 
        
        return root 

          
        