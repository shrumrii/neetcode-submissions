class MinStack:

    def __init__(self):
        self.items = []
        self.min_track = []
        

    def push(self, val: int) -> None: 
        self.items.append(val)
        if not self.min_track: #empty 
            self.min_track.append(val)
        else: 
            minimum = self.getMin()
            if val > self.getMin(): #not minimum
                self.min_track.append(minimum)
            else: 
                self.min_track.append(val)

    def pop(self) -> None:
        if self.items: 
            self.items.pop() 
            self.min_track.pop() 
        

    def top(self) -> int:
        if self.items: 
            top = self.items[-1]
            return top
        else: 
            return None 

    def getMin(self) -> int:
        if self.min_track: 
            return self.min_track[-1]
        else: 
            return None 
    
        
