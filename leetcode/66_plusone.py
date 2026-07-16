class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = digits[-1] + 1
        digits[-1] = a % 10
        carry = a // 10
        for i in range(len(digits) - 2, -1, -1):
            if carry == 0:
                break
            a = digits[i] + carry
            digits[i] = a % 10
            carry = a // 10
        if carry:
            digits.insert(0, carry)
        return digits