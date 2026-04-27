class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        length = len(nums)
        global_max = nums[0]

        def util(curr_index, curr_sum, nums):  
            nonlocal global_max

            #break
            if curr_index == length:  
                return
            
            #recursive case 
            new_sum = curr_sum + nums[curr_index]
            curr_sum = max(nums[curr_index], new_sum)
            global_max = max(curr_sum, global_max)

            return util(curr_index+1, curr_sum, nums)
            
        util(0, 0, nums)
        return global_max
                
