class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0 
        heights_len = len(heights)
        right = heights_len - 1  

        while True: 

            #break 
            if right <= left: 
                break 
            
            height = min(heights[left], heights[right])
            length = right - left 
            product = height * length 

            if product >= max_area: 
                max_area = product 

            print(f'Right pointer index:{right}, Left pointer index:{left}, product: {product}')

            if heights[left] >= heights[right]:
                right -= 1 
            else: 
                left += 1 
        
        return max_area 



            

        


