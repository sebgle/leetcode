# Last updated: 7/16/2025, 9:42:26 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = curr = maxLength = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            maxLength = max(maxLength, (right - left + 1))
        return maxLength