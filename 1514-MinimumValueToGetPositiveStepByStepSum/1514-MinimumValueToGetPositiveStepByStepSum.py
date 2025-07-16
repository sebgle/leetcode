# Last updated: 7/16/2025, 9:42:11 AM
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        currSum = lowestPoint = 0
        for i in range(len(nums)):
            currSum += nums[i]
            lowestPoint = min(lowestPoint, currSum)
        if lowestPoint < 0:
            return abs(lowestPoint) + 1
        else:
            return 1
        