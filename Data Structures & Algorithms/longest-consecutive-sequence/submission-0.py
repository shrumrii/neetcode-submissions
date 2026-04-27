class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res_list = []
        maximum = 0 

        nums_dict = {} 
        for num in nums: 
            nums_dict[num] = nums_dict.get(num, 0) + 1 

        maximum = 0
        curr_num = 0 
        i = 0 

        maximum = 0 
        
        for num in nums_dict: 

            if num-1 not in nums_dict: 
                current_sequence = 0 
                i = num
                while True: 

                    #break when next num not in dict
                    if i not in nums_dict: 
                        break 
                    i += 1 
                    current_sequence += 1
                
                if current_sequence >= maximum: 
                    maximum = current_sequence 
        return maximum
                    
                    
            



        