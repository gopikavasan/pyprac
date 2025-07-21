# https://leetcode.com/problems/pascals-triangle-ii/description/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        prev = 1
        for k in range(1, rowIndex+1):
            next_val = (prev * ((rowIndex)-k+1))//k
            row.append(next_val)
            prev = next_val
        return row
        
