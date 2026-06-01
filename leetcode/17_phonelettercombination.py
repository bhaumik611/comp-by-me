'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.'''
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_char = {
            2 : 'abc',
            3 : 'def',
            4 : 'ghi',
            5 : 'jkl',
            6 : 'mno',
            7 : 'pqrs',
            8 : 'tuv',
            9 : 'wxyz'
        }
        res = []
        def backtrack(i, path):
            if i == len(digits):
                res.append(path)
                return
            for char in digit_to_char[int(digits[i])]:
                backtrack(i+1, path+char)
        backtrack(0, '')
        return res
    
sol = Solution()
print(sol.letterCombinations("23"))