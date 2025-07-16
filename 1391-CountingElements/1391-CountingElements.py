# Last updated: 7/16/2025, 9:42:16 AM
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        seen = set(arr)
        for number in arr:
            if number + 1 in seen:
                count += 1
        return count