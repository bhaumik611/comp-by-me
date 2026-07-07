'''You are given two strings s and t consisting of lowercase English letters.

You may choose at most one index in s and replace the character at that index with any lowercase English letter.

Return true if it is possible to make s a subsequence of t; otherwise, return false.

 

Example 1:

Input: s = "cat", t = "chat"

Output: true

Explanation:

Replace s[1] from 'a' to 'h'. The resulting string is "cht".
"cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.
Example 2:

Input: s = "plane", t = "apple"

Output: false

Explanation:

The characters 'p', 'l', and 'e' can be matched in t, but the remaining characters cannot be matched while preserving the required order.
Even after replacing any one character in s, it is impossible to make s a subsequence of t.
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist only of lowercase English letters.'''

class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i = j = 0
        
        # Check if s is already a subsequence of t
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        if i == m:
            return True
        
        # Try replacing each character in s and check if it becomes a subsequence of t
        for k in range(m):
            original_char = s[k]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == original_char:
                    continue
                new_s = s[:k] + c + s[k+1:]
                i = j = 0
                while i < m and j < n:
                    if new_s[i] == t[j]:
                        i += 1
                    j += 1
                if i == m:
                    return True
        
        return False