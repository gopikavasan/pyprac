# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        mydict = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        mysum = 0
        for i in range(len(s)):
            if i < len(s)-1 and mydict[s[i]] < mydict[s[i+1]]:
                mysum-=mydict[s[i]]
            else:
                mysum+=mydict[s[i]]
        return mysum



