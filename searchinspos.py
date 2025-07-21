# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target :
                return i
            elif nums[i] < target:
                k = i
        return  k+1
