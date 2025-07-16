# Last updated: 7/16/2025, 9:42:05 AM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for character in sentence:
            seen.add(character)
        return len(seen) == 26