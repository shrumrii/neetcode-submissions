class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy = {} 
        for i in range(len(nums)): 
            difference = target - nums[i]
            if difference in mappy: 
                return [mappy[difference], i] 
            
            mappy[nums[i]] = i