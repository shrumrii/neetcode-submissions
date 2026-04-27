class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0 
        row = len(grid)
        col = len(grid[0])

        for r in range(row): 
            for c in range(col): 
                if grid[r][c] == '1': 
                    islands += 1 

                    stack = [(r,c)]
                    grid[r][c] = '0'

                    #start iterative dfs 
                    while stack: 
                        coord_r, coord_c = stack.pop()

                        #check neighbors 
                        top_r, top_c = coord_r - 1, coord_c 
                        left_r, left_c = coord_r, coord_c - 1
                        right_r, right_c = coord_r, coord_c + 1 
                        down_r, down_c = coord_r + 1, coord_c 

                        #boundary check 
                        directions = [(top_r, top_c), (left_r, left_c), (right_r, right_c), (down_r, down_c)]
                        for neighbor_r, neighbor_c in directions:
                            if 0 <= neighbor_r < row and 0 <= neighbor_c < col and grid[neighbor_r][neighbor_c] == '1': 
                                stack.append((neighbor_r, neighbor_c)) 
                                grid[neighbor_r][neighbor_c] = '0' 
        return islands 


                
                
