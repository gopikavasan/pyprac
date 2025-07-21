# https://leetcode.com/problems/pascals-triangle/description/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for rowNum in range(numRows):
            row = [None] * (rowNum + 1)  # Correct row length

            row[0] = 1
            row[-1] = 1

            for i in range(1, rowNum):
                row[i] = triangle[rowNum - 1][i - 1] + triangle[rowNum - 1][i]

            triangle.append(row)

        return triangle
        
