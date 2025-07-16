# Last updated: 7/16/2025, 9:42:23 AM
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numbers = defaultdict(int)
        curr = -1
        for number in nums:
            numbers[number] += 1
        for number in numbers:
            if numbers[number] == 1 and number > curr:
                curr = number
        return curr