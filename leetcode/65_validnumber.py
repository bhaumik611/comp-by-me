'''Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.'''

from typing import List

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        num_seen = False
        dot_seen = False
        e_seen = False
        for i, char in enumerate(s):
            if char.isdigit():
                num_seen =True
            elif char in ['+', '-']:
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif char == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif char in ['e', 'E']:
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False
            else:
                return False
        return num_seen
    
sol = Solution()
print(sol.isNumber("0"))