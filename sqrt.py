# https://leetcode.com/problems/sqrtx/description/
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 :
            return 0
        threshold = 0.000001
        guess = x/2.0
        while True:
            next_guess = (guess + x/guess)/2
            if abs(next_guess-guess) < threshold :
                return int(next_guess)
            guess = next_guess
