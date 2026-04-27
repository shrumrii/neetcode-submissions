class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0 
        length = len(numbers)
        right = length - 1 

        while True: 

            #break 
            if right < left: 
                return [-1, -1]

            check_sum = numbers[left] + numbers[right]
            if check_sum == target:  
                return [left+1, right+1] 
            elif check_sum > target: 
                right -= 1
            else: 
                left += 1 

            