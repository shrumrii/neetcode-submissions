class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [] 
        mappy = {} 
        for index, num in enumerate(nums): 
            difference = target - num 
            if difference in mappy:  
                return [mappy[difference], index] 
            mappy[num] = index
