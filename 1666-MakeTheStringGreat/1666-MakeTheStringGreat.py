# Last updated: 7/16/2025, 9:42:06 AM
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif c.islower() and stack[-1] == c.upper():
                stack.pop()
            elif c.isupper() and stack[-1] == c.lower():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)