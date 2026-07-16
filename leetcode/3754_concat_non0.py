class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = int(str(n).replace('0', ''))
        total_sum = sum(int(digit) for digit in str(n))
        total_product = 1
        total_product = total_sum * n
        return total_product

sol = Solution()
n = sol.sumAndMultiply(10203004)
print(n)