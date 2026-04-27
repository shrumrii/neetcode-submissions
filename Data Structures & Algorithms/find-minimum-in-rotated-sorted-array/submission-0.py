class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums) - 1 
        n = len(nums) 

        #just do binary search  
        while low < high: 

            if nums[low] < nums[high]: #done 
                return nums[low]

            mid = (low + high) // 2 

            if nums[mid] > nums[high]: #go to right section, not sorted and where the minimum is 
                low = mid + 1 

            else: 
                high = mid 

        return nums[low]