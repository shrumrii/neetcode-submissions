class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        max_length = 0 

        for i, char in enumerate(s):
         
            if char in s[left:i]: 
                left = s.find(char, left) + 1 

            substring_length = i - left + 1 
            if substring_length > max_length: 
                max_length = substring_length 
            
        return max_length 
