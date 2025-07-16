# Last updated: 7/16/2025, 10:00:19 AM
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        curr, ans = 0, 0
        for box in sorted(boxTypes, key = itemgetter(1), reverse = True):
            amt = box[0]
            while curr < truckSize and amt > 0:
                curr += 1
                ans += box[1]
                amt -= 1
        return ans
            