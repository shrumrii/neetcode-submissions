class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        length = len(cost)
        memo = {}

        def solve(i): 

            if i >= length: 
                return 0 

            if i in memo: 
                return memo[i]
            
            min_res = cost[i] + min(solve(i+1), solve(i+2)) 
            memo[i] = min_res
            return min_res

        return min(solve(0), solve(1))
        