from ast import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i>>1) for i in range(1<<n)]
    
sol = Solution()
a = sol.grayCode(2)
print(a)