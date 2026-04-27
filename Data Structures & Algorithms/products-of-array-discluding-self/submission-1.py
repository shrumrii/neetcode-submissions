class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums) 
        left = [1]*length 
        right = [1]*length 

        for i in range(length): 
            if i == 0: 
                continue 

            left[i] = nums[i-1] * left[i-1]
    
        for i in range(length - 1, -1, -1): 
            if i == length - 1: 
                continue 
            right[i] = nums[i+1] * right[i+1]

        for i in range(length): 
            left[i] = left[i] * right[i]

        return left