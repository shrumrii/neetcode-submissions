class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j, nums): 
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp 

        left = 0 
        right = len(nums)-1 
        pointer = 0 

        while True: 

            #break 
            if pointer > right: 
                break 
            
            if nums[pointer] == 0: 
                swap(left, pointer, nums) 
                left += 1
                pointer += 1
            elif nums[pointer] == 1: 
                pointer += 1
            else: 
                swap(right, pointer, nums)
                right -= 1 
            
        