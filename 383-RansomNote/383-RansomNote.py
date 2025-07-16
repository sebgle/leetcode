# Last updated: 7/16/2025, 9:42:47 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)
        for letter in sorted(magazine):
            mag[letter] += 1
        for letter in sorted(ransomNote):
            if letter in mag:
                mag[letter] -= 1
                if mag[letter] == 0:
                    del mag[letter]
            else:
                return False
        return True