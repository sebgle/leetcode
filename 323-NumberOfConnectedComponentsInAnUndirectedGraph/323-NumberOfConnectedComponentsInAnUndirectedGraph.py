# Last updated: 7/16/2025, 9:42:51 AM
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for child in graph[node]:
                dfs(child)
        
        count = n - len(graph)
        seen = set()
        
        for node in graph:
            if node not in seen:    
                dfs(node)
                count += 1
        
        return count