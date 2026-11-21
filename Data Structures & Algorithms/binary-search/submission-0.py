class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            ans = nums.index(target)
        except ValueError:
            ans = -1

        return ans

        # lo, hi = 0, len(nums)-1
        # mid = (lo + hi)//2
        # while lo <= hi:
        #     if target == nums[mid]:
        #         return mid
        #     elif target < nums[mid]:
        #         hi = mid - 1
        #     elif target > nums[mid]:
        #         lo = mid + 1

        
        