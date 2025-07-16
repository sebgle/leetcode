# Last updated: 7/16/2025, 10:57:51 AM
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = Counter(arr)
        goal, curr, ans = len(arr) // 2, len(arr), 0
        for num in sorted(frequency.items(), key=lambda item:item[1], reverse=True):
            curr -= num[1]
            ans += 1
            if curr <= goal:
                return ans