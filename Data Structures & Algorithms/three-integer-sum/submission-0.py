class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lis = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for z in range(len(nums)):
                    a = nums[i] + nums[j] + nums[z]
                    if a == 0 and i!=j!=z!=i:
                        l = [nums[i], nums[j], nums[z]]
                
                        lis.append(sorted(l))
        liss = [list(j) for j in set(tuple(k) for k in lis)]
        return liss
        