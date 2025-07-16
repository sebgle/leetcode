# Last updated: 7/16/2025, 9:42:37 AM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelCount = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewelCount:
                count += 1
        return count
        