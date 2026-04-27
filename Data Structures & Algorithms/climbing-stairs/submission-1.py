class Solution:
    def climbStairs(self, n: int) -> int:

        def dpclimbStairs(n, memo) -> int: 

            if memo[n] is not None: 
                return memo[n]
            #base 
            if n == 1: 
                return 1

            if n == 2: 
                return 2 
            
            ways = dpclimbStairs(n-1, memo) + dpclimbStairs(n-2, memo)
            memo[n] = ways
            return ways 

        memo = [None]*(n+1)
        answer = dpclimbStairs(n, memo)
        return answer

        



        # count = 0 

        # #base case 
        # if n == 1: 
        #     return 1 

        # if n == 2: 
        #     return 2 

        # return self.climbStairs(n-1) + self.climbStairs(n-2)