# Last updated: 7/16/2025, 9:42:07 AM
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = defaultdict(list)
        x, y = 0, 0
        seen[-1] = [x,y]
        for i in range(len(path)):
            if path[i] == 'N':
                y += 1
            elif path[i] == 'E':
                x += 1
            elif path[i] == 'S':
                y -= 1
            else:
                x -= 1
            if [x,y] in seen.values():
                return True
            seen[i] = [x,y]
        return False
