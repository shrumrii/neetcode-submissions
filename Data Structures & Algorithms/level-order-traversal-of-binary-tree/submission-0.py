# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_list = [] 

        queue = deque() 
        queue.append(root)

        while queue: 

            length = len(queue)
            level_list = [] 

            #process each level of nodes 
            for i in range(length): 
                popped_node = queue.popleft()
                if popped_node is None: 
                    continue 
                level_list.append(popped_node.val)
                #add left and right children nodes 
                queue.append(popped_node.left)
                queue.append(popped_node.right) 
            
            #append level list to res_list
            if level_list: 
                res_list.append(level_list)

        return res_list 

            