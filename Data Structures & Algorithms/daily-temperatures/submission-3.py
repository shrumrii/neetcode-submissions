class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = len(temperatures) 
        result = [0]*t

        stack = [] 
        for i in range(t): 
            curr_temp = temperatures[i]
            while stack: 
                prev_index = stack[-1] 
                
                #pop previous index and add to results if current temp is greater 
                if curr_temp > temperatures[prev_index]: 
                    result[prev_index] = i - prev_index 
                    stack.pop()
                else: 
                    break 

            #add curr index to stack 
            stack.append(i)
        return result 

            

