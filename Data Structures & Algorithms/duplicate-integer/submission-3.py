class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {} 
        for num in nums: 
            if num not in nums_dict: 
                nums_dict[num] = 1 
            else: 
                nums_dict[num] += 1 
        
        for val in nums_dict.values(): 
            if val > 1: 
                return True
        
        return False