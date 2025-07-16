# Last updated: 7/16/2025, 9:42:17 AM
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        records = defaultdict(int)
        answer = [[],[]]
        for match in matches:
            records[match[1]] += 1
            records[match[0]] += 0
        for player in records:
            if records[player] == 0:
                answer[0].append(player)
            elif records[player] == 1:
                answer[1].append(player)
        return sorted(answer[0]), sorted(answer[1])