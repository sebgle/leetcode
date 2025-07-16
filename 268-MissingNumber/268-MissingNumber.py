# Last updated: 7/16/2025, 9:42:53 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        for number in range(len(nums) + 1):
            if number not in seen:
                return number