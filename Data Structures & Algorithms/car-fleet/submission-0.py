class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #create new sorted position (with speed) - tuple 
        new_position = [(p, s) for p, s in zip(position, speed)]
        sorted_position = sorted(new_position, reverse=True)

        #initialize time to take array
        time_to_take = []
        for i in range(len(sorted_position)): 
            pos = sorted_position[i][0]
            speed = sorted_position[i][1]

            time = (target - pos) / speed 
            time_to_take.append(time) 

        stack = [] 
        for time in time_to_take: 

            if not stack: 
                stack.append(time) 
            
            peek = stack[-1]
            if time <= peek: 
                pass 
            else: 
                #new fleet has been created 
                stack.append(time) 

        return len(stack)

            

