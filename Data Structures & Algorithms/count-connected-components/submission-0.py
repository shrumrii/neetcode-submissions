class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0 
        
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v) 
            adj[v].append(u)

        visited = [] 
        for i in range(n):  
            
            if len(visited) == n: 
                return count
            
            if i in visited: 
                continue
            
            #run dfs 
            stack = [i]

            while stack: 
                
                v = stack.pop() 
                if v not in visited: 
                    visited.append(v)
                    for neighbor in adj[v]: 
                        stack.append(neighbor)
            count += 1 

        return count

            