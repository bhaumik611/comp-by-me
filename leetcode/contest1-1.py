'''You are given a positive integer n.

Let digitSum be the sum of the digits of n, and let squareSum be the sum of the squares of the digits of n.

An integer is called good if squareSum - digitSum >= 50.

Return true if n is good. Otherwise, return false.

'''

class Solution:
    def isGood(self, n: int) -> bool:
        digit_sum = sum(int(digit) for digit in str(n))
        square_sum = sum(int(digit) ** 2 for digit in str(n))
        return square_sum - digit_sum >= 50