class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: 
            return False

        opening = '({['
        closing = ')]}'
        stack = []
        for char in s: 
            if char in opening:
                stack.append(char)
            elif char in closing: 
                if not stack: 
                    return False 
                top = stack[-1] 
                if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'): 
                    return False 
                stack.pop() 

        if not stack: 
            return True 
        else: 
            return False

        