class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while (True): 

            #break when no numbers left
            if n == 0: 
                break 

            if (n & 1) == 1: 
                count += 1 

            #keep shifting right
            n >>= 1
        return count 