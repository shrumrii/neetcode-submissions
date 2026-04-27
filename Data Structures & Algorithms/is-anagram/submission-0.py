class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDictS = {} 
        charDictT = {} 
        for letter in s: 
            if letter in charDictS: 
                charDictS[letter] += 1 
            else: 
                charDictS[letter] = 1 
        
        for letter in t: 
            if letter in charDictT: 
                charDictT[letter] += 1 
            else: 
                charDictT[letter] = 1

        if charDictS == charDictT: 
            return True
        else: 
            return False  
        
        