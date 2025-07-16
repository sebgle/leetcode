# Last updated: 7/16/2025, 9:42:40 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = curr = answer = 0
        for right in range(len(nums)):
            curr += nums[right]
            while (right - left + 1) > k:
                curr -= nums[left]
                left += 1
            if (right - left + 1) == k:
                if answer == 0:
                    answer = curr / k
                else:
                    answer = max(answer, curr / k)
        return answer
            