# Last updated: 7/16/2025, 9:42:04 AM
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        ans = 0
        for num in nums:
            seen[num] += 1
            if seen[num] == 1:
                ans += num
            elif seen[num] == 2:
                ans -= num
        return ans