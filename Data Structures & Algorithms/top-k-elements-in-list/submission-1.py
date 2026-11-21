class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
         
        for a in nums:
            if a in dicti:

                dicti[a] += 1
            
            else: 
                dicti[a] = 1

        sorted_desc = dict(sorted(dicti.items(), key=lambda item: item[1], reverse=True))
        first_n_keys = list(sorted_desc.keys())[:k]
        return first_n_keys

        
        
        