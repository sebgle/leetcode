# Last updated: 7/16/2025, 9:43:14 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = longest = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        return longest