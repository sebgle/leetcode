# Last updated: 7/16/2025, 9:42:19 AM
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = defaultdict(int)
        for letter in "balloon":
            balloon[letter] += 1
        newBalloon = defaultdict(int)
        for letter in text:
            if letter in balloon:
                newBalloon[letter] += 1
        if len(newBalloon) != len(balloon):
            return 0
        maxBalloon = len(text)
        for letter in newBalloon:
            if newBalloon[letter] // balloon[letter] < maxBalloon:
                maxBalloon = newBalloon[letter] // balloon[letter]
        return maxBalloon