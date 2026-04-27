class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        rows = len(grid)  
        cols = len(grid[0])

        for i in range(rows): 
            for j in range(cols): 

                #is island 
                if grid[i][j] == 1: 
                    
                    grid[i][j] = 0
                    count = 0 
                    stack = [(i,j)]

                    while stack: 
                        
                        count += 1 
                        curr_r, curr_c = stack.pop() 
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
                            nr = curr_r + dr 
                            nc = curr_c + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: 
                                stack.append((nr, nc))
                                grid[nr][nc] = 0 
                    
                    if count >= max_area: 
                        max_area = count

        return max_area
                            



        
                            
                        




                

                
