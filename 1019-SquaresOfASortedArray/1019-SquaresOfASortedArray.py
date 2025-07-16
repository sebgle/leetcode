# Last updated: 7/16/2025, 9:42:27 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        i, j = 0, n - 1
        for x in range(n - 1, -1, -1):
            if abs(nums[i]) < abs(nums[j]):
                answer[x] = nums[j] * nums[j]
                j -= 1
            else:
                answer[x] = nums[i] * nums[i]
                i += 1
        return answer