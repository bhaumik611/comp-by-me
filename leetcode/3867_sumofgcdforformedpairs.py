'''You are given an integer array nums of length n.

Construct an array prefixGcd where for each index i:

Let mxi = max(nums[0], nums[1], ..., nums[i]).
prefixGcd[i] = gcd(nums[i], mxi).
After constructing prefixGcd:

Sort prefixGcd in non-decreasing order.
Form pairs by taking the smallest unpaired element and the largest unpaired element.
Repeat this process until no more pairs can be formed.
For each formed pair, compute the gcd of the two elements.
If n is odd, the middle element in the prefixGcd array remains unpaired and should be ignored.
Return an integer denoting the sum of the GCD values of all formed pairs.

The term gcd(a, b) denotes the greatest common divisor of a and b.'''

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n
        mxi = nums[0]
        prefixGcd[0] = nums[0]

        for i in range(1, n):
            mxi = max(mxi, nums[i])
            prefixGcd[i] = self.gcd(nums[i], mxi)

        prefixGcd.sort()
        total_gcd_sum = 0

        for i in range(n // 2):
            total_gcd_sum += self.gcd(prefixGcd[i], prefixGcd[n - 1 - i])

        return total_gcd_sum

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    