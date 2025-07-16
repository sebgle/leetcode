# Last updated: 7/16/2025, 9:42:44 AM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = ans = 0
        map = defaultdict(int)
        map[count] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else: 
                count += 1
            if count in map:
                ans = max(ans, i - map[count])
            else:
                map[count] = i
        return ans