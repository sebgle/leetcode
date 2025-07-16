# Last updated: 7/16/2025, 9:41:54 AM
class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s) - 1):
            print(ord(s[i]), ord(s[i + 1]))
            ans += abs(ord(s[i]) - ord(s[i + 1]))
        return ans