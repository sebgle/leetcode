# Last updated: 7/16/2025, 9:42:10 AM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        ans = []
        for num in nums:
            ans.append(num + curr)
            curr += num
        return ans