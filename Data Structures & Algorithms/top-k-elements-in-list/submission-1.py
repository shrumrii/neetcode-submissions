class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_list = []
        buckets = []
        k_dict = defaultdict()

        for num in nums: 
            k_dict[num] = 1 + k_dict.get(num, 0) 

        buckets = [[] for i in range(len(nums) + 1)]

        for number, freq in k_dict.items(): 
            buckets[freq].append(number) 

        for i in range(len(buckets)-1, 0, -1): 
            for n in buckets[i]: 
                res_list.append(n) 

                if len(res_list) == k: 
                    return res_list 

        
