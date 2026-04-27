class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [] 
        anagram_map = dict() 

        for word in strs:

            count = [0]*26 

            for char in word: 
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)
            if key not in anagram_map:
                anagram_map[key] = [word]
            else: 
                anagram_map[key].append(word)
        
        for word in anagram_map.values():
            res.append(word)

        return res 
            
            
        
        

