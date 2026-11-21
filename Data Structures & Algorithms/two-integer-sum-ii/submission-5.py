class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lis = []
        for i in range(len(numbers)):
            g = target - numbers[i]
            
            if g in numbers and (i+1) != (numbers.index(g)+1):
               
                o = [i+1, numbers.index(g)+1] 

                lis.append(sorted(o))

        unique_data = [list(t) for t in set(tuple(i) for i in lis)]
        for j in unique_data:
            return j