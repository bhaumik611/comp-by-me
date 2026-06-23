'''Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 '''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"
        
        m,n = len(num1), len(num2)
        res = [0] * (m+n)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum = mul + res[i+j+1]
                res[i+j+1] = sum % 10
                res[i+j] += sum // 10
        
        result = []
        for num in res:
            if not (len(result) == 0 and num == 0):
                result.append(str(num))
        return ''.join(result)
    