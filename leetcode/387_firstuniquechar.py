class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for ch in s:
            char_count[ch] = char_count.get(ch, 0) + 1
            
        for i, ch in enumerate(s):
            if char_count[ch] == 1:
                return i

        return -1