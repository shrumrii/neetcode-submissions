class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
         
        adj = defaultdict(list)
        for u,v in prerequisites: 
            adj[u].append(v) #directed 

        visited = [] 
        current_path = []

        def hasCycle(v): 
            if v in current_path: 
                return True 
            
            if v in visited: 
                return False 
            
            visited.append(v) 
            current_path.append(v) 

            for neighbor in adj[v]: 
                if hasCycle(neighbor): 
                    return True 

            current_path.remove(v)         
            return False 

        for i in range(numCourses): 
            if i not in visited:  
                if hasCycle(i): 
                    return False  


        return True

    


        