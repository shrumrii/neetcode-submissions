class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean string 
        clean_string = ""
        for element in s.lower(): 
            if element.isalnum(): 
                clean_string += element
        print(clean_string)
        charArray = list(clean_string) 
        length = len(charArray)
        left = 0 
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

                