# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b= 0,1
        sum1 = 0
        for i in range(n):
            sum1 = a+b
            a = b
            b = sum1
        return sum1
        
