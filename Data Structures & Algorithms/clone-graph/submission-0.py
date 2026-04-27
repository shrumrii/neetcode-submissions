"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: 
            return None 

        adjDict = {node: Node(node.val)}
        visited = []
        stack = [node]

        while stack: 

            v = stack.pop() 
            
            for neighbor in v.neighbors: 
                
                if neighbor not in adjDict: 
                    adjDict[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                adjDict[v].neighbors.append(adjDict[neighbor])

        return adjDict[node]
                

        