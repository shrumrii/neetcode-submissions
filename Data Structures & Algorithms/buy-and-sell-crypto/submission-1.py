class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1 
        max_neet = 0 
        while True: 

            #break 
            if right >= len(prices): 
                break 

            neet = prices[right] - prices[left]
            if neet > max_neet:
                max_neet = neet

            #keep looking for higher profit 
            if prices[left] < prices[right]: 
                right += 1 
                continue 
            
            left += 1 
            if left == right: 
                right += 1 
        
        return max_neet 




