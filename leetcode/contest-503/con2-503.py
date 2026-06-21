'''You are given a string password.

The strength of the password is calculated based on the following rules:

1 point for each distinct lowercase letter ('a' to 'z').
2 points for each distinct uppercase letter ('A' to 'Z').
3 points for each distinct digit ('0' to '9').
5 points for each distinct special character from the set "!@#$".
Each character contributes at most once, even if it appears multiple times.

Return an integer denoting the strength of the password.

 

Example 1:

Input: password = "aA1!"

Output: 11

Explanation:

The distinct characters are 'a', 'A', '1' and '!'.
Thus, the strength = 1 + 2 + 3 + 5 = 11.
Example 2:

Input: password = "bbB11#"

Output: 11

Explanation:

The distinct characters are 'b', 'B', '1' and '#'.
Thus, the strength = 1 + 2 + 3 + 5 = 11.​​​​​​​'''

class Solution:
    def passwordStrength(self, password: str) -> int:
        distinct_chars = set(password)
        strength = 0
        
        for char in distinct_chars:
            if char.islower():
                strength += 1
            elif char.isupper():
                strength += 2
            elif char.isdigit():
                strength += 3
            elif char in "!@#$":
                strength += 5
        
        return strength
    
strength_calculator = Solution()
strength1 = strength_calculator.passwordStrength("aA1!")
print(strength1)  