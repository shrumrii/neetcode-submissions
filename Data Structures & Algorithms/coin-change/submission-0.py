class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def coinChangeRecursive(new_amount) -> int: 
            
            #base case 
            if new_amount == 0: 
                return 0 

            if new_amount < 0: 
                return float('inf')

            if new_amount in memo: 
                return memo[new_amount]

            min_coins = float('inf')
            for coin in coins: 
                difference = new_amount - coin
                num_coins = coinChangeRecursive(difference)
                if num_coins != float('inf'): 
                    min_coins = min(min_coins, num_coins + 1)
            
            memo[new_amount] = min_coins
            return min_coins
    
        num_coins = coinChangeRecursive(amount)
        if num_coins == float('inf'): 
            return -1
        else: 
            return num_coins



                
            
        
            

        
        res = coinChangeRecursive(amount)
        return res 
            

            