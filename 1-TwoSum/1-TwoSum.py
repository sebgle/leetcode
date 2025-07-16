# Last updated: 7/16/2025, 9:43:15 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in indices:
                return [indices[target - nums[i]], i]
            indices[nums[i]] = i
        