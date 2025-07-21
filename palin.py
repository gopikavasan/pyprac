# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        mystring = [e for e in str(x)]
        return mystring == mystring[::-1]
        
