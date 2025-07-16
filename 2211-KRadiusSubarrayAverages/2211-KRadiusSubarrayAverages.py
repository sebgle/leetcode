# Last updated: 7/16/2025, 9:41:59 AM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = []
        prefixSum = []
        currSum = 0
        for num in nums:
            currSum += num
            prefixSum.append(currSum)            
        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(nums):
                if i - k > 0:
                    ans.append((prefixSum[i + k] - prefixSum[i - k - 1]) // (k*2+1))
                else:
                    ans.append((prefixSum[i + k] // (k*2+1)))
            else:
                ans.append(-1)
        return ans