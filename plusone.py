# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(e) for e in digits])) + 1
        return ([int(n) for n in str(num)])
        
