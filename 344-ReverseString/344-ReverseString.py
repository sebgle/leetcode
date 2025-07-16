# Last updated: 7/16/2025, 9:42:49 AM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(s, l, h):
            if h < l:
                return
            s[l], s[h] = s[h], s[l]
            helper(s, l + 1, h - 1)
        helper(s, 0, len(s) - 1)