class Solution:
    def reverse(self, x: int) -> int:
        res = ''
        a = list(str(abs(x)))
        a.reverse()
        temp = str(''.join(a))
        if x < 0:
            res+='-'
        
        return int(res+temp) if -2**31 <= int(res+temp) <= 2**31-1 else 0
    
sol = Solution().reverse(1534236469)
print(sol)