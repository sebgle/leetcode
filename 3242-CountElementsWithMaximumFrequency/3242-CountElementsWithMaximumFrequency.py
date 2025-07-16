# Last updated: 7/16/2025, 9:41:56 AM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        maxfreq = len(nums)
        count = 0
        for num in nums:
            seen[num] += 1
        for value in seen.values():
            if value == maxfreq:
                count += maxfreq
            elif value != maxfreq:
                if maxfreq not in seen.values():
                    maxfreq = value
                    count = maxfreq
                elif value > maxfreq:
                    maxfreq = value
                    count = maxfreq
        return count
            

        