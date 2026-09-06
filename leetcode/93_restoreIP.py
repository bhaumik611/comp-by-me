from git import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s: str, start: int, path: List[str], res: List[str]):
        if len(path) == 4:
            if start == len(s):
                res.append('.'.join(path))
            return

        for i in range(1,4):
            if start + i > len(s):
                break
            segment = s[start:start+i]
            if (segment[0] == '0' and len(segment) > 1) or (i == 3 and int(segment) > 255):
                continue
            self.dfs(s, start+i, path + [segment], res)

        return

sol = Solution()
# Test cases
print(sol.restoreIpAddresses("25525511135"))
print(sol.restoreIpAddresses("0000"))