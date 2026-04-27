class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def rob_recursive(index, nums: List[int]) -> int: 
            
            if index in memo: 
                return memo[index]

            if index >= len(nums):
                return 0

            compare1 = nums[index] + rob_recursive(index+2, nums)
            compare2 = rob_recursive(index+1, nums)
            large = max(compare1, compare2)
            memo[index] = large
            return large 

        maximum = rob_recursive(0, nums)
        return maximum
        


        