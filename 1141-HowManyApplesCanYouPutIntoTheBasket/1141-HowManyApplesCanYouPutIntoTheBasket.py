# Last updated: 7/16/2025, 10:57:56 AM
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        curr, i, ans = 0, 0, 0
        apples = sorted(weight)
        for apple in apples:
            if curr + apple <= 5000:
                curr += apple
                ans += 1
            else:
                break
        return(ans)
            
            
        