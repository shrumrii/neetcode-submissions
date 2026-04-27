class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} 

        def wordBreakRecursive(substring: str) -> bool: 

            #check memo
            if substring in memo:
                return memo[substring]
        
            #base case - true 
            if not substring: 
                return True 
    
            #recursive case 
            for word in wordDict: 
                if substring.startswith(word): 
                    remaining = substring[len(word):]
                    if wordBreakRecursive(remaining): 
                        memo[substring] = True
                        return True
        
            #no word worked, return false 
            memo[substring] = False
            return False
    
        return wordBreakRecursive(s) 