'''Given an integer array nums, return the length of the longest subarray that has a bitwise XOR of zero and contains an equal number of even and odd numbers. If no such subarray exists, return 0.'''

from ast import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_xor = [0] * (n + 1)
        even_count = [0] * (n + 1)
        odd_count = [0] * (n + 1)

        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ nums[i]
            even_count[i + 1] = even_count[i] + (nums[i] % 2 == 0)
            odd_count[i + 1] = odd_count[i] + (nums[i] % 2 != 0)

        max_length = 0
        xor_map = {}

        for i in range(n + 1):
            key = (prefix_xor[i], even_count[i] - odd_count[i])
            if key in xor_map:
                max_length = max(max_length, i - xor_map[key])
            else:
                xor_map[key] = i

        return max_length