class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0 
        max_count = 0
        length = len(s)

        counts_dict = {} 
        max_frequency = 0 
        
        while True: 
            
            #break 
            if right >= length: 
                break

            right_letter = s[right]
            counts_dict[right_letter] = counts_dict.get(right_letter, 0) + 1 
            max_frequency = max(max_frequency, counts_dict[right_letter])
            
            #check window invalid 
            while (right - left + 1) - max_frequency > k: 
                counts_dict[s[left]] -= 1  
                left += 1 

            current_count = right - left + 1 
            if current_count > max_count: 
                max_count = current_count 
            
            right += 1 

        return max_count 

