from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()

        ptr = 1
        max_diff = 0

        while ptr < len(nums):
            diff = nums[ptr] - nums[ptr-1]
            if diff > max_diff:
                max_diff = diff
            ptr += 1

        return max_diff

sol = Solution()
print(sol.maximumGap([3,6,9,1]))