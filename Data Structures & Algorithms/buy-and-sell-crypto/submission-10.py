class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lis = []
        for i in range(len(prices)):
            for j in range(len(prices)):
                
                if i < j:
                    a = prices[j] - prices[i]
                    lis.append(a)
                else:
                    lis.append(0)
        return max(lis)
        


        