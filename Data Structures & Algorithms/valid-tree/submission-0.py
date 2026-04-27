class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1: 
            return False 

        #tree must have only 2 children 
        #not a cycle 
        adj = defaultdict(list) 
        for u,v in edges: 
            adj[u].append(v)
            adj[v].append(u) 

        visited = [] 
        stack = [0] 

        while stack: 
            
            node = stack.pop()
            
            if node not in visited: 
                visited.append(node) 
                for element in adj[node]: 
                    stack.append(element) 
        
        print(len(visited))
        if len(visited) != n: 
            return False 

        return True 


