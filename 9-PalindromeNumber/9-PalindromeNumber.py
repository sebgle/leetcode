# Last updated: 7/24/2025, 7:49:47 AM
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        prev = s[len(s) - 1]
        total = 0
        for numeral in reversed(s):
            if dic[prev] > dic[numeral]:
                total -= dic[numeral]
            else:
                total += dic[numeral]
            print(total)
            prev = numeral
        return total