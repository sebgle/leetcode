# Last updated: 7/16/2025, 9:42:41 AM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        seen = set()
        ans = 0

        for i in range(len(isConnected)):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        
        return ans


            
        