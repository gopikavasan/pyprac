# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[k]:
                nums[i],nums[k+1] = nums[k+1], nums[i]
                k+=1
        return k+1

        
