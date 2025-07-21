# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {')':'(', '}':'{', ']':'['}
        mylist = []
        for i in range(len(s)):
            if s[i] not in mydict:
                mylist.append(s[i])
            else:
                if not mylist or mylist[-1] != mydict[s[i]]:
                    return False
                mylist.pop()

                #print (s[i], mylist, mydict[s[i]])
        return len(mylist) == 0


