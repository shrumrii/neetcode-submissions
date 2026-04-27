class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(sa: str) -> bool:
            charArray = list(sa) 
            left = 0 
            length = len(sa) 
            right = length-1 
            while True: 

                #break when middle, so 
                if left > right: 
                    break 
            
                #compare left and right
                if charArray[left] != charArray[right]: 
                    return False 
                else: 
                    left += 1 
                    right -= 1 

            return True 

        curr_string = '' 
        memo = {}
        for i in range(len(s)): 
            for j in range(len(s)): 
                string = s[i:j+1]
                if string not in memo: 
                    bool_value = isPalindrome(string)
                    memo[string] = bool_value 
                    if len(string) > len(curr_string) and bool_value: 
                        curr_string = string 
                else: 
                    pass 

        return curr_string

            

        
            
            


            




