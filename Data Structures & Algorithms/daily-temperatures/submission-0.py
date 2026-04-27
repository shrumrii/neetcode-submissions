class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [] 
        for i in range(len(temperatures)):
            print('i', i)  

            if i == len(temperatures)-1: 
                result.append(0) 
            
            for j in range(i+1, len(temperatures)): 
                
                print('j', j) 
                if temperatures[i] >= temperatures[j]: 
                    if i == len(temperatures)-1 or j == len(temperatures)-1: 
                        result.append(0) 
                        break
                    else: 
                        continue 
   
                else: 
                    counter = j - i 
                    result.append(counter)
                    break 


        return result