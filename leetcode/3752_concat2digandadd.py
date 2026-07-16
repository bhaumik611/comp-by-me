from typing import List
import bisect

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        nonzero_positions = []
        nonzero_digits = []

        for i, ch in enumerate(s):
            if ch != "0":
                nonzero_positions.append(i)
                nonzero_digits.append(int(ch))

        m = len(nonzero_digits)
        prefix_sum = [0] * (m + 1)
        prefix_concat = [0] * (m + 1)
        pow10 = [1] * (m + 1)

        for i in range(m):
            prefix_sum[i + 1] = prefix_sum[i] + nonzero_digits[i]
            prefix_concat[i + 1] = (prefix_concat[i] * 10 + nonzero_digits[i]) % mod
            pow10[i + 1] = (pow10[i] * 10) % mod

        ans = []
        for l, r in queries:
            left = bisect.bisect_left(nonzero_positions, l)
            right = bisect.bisect_right(nonzero_positions, r) - 1
            if left > right:
                ans.append(0)
                continue

            count = right - left + 1
            x = prefix_concat[right + 1] - prefix_concat[left] * pow10[count] % mod
            x %= mod
            digit_sum = prefix_sum[right + 1] - prefix_sum[left]
            ans.append((x * digit_sum) % mod)

        return ans
