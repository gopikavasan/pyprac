# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            if target - nums[i] not in mydict :
                mydict[nums[i]] = i
            else :
                return [i, mydict[target - nums[i]]]
