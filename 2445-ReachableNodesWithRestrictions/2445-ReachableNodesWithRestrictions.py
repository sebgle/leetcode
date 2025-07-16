# Last updated: 7/16/2025, 9:41:58 AM
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        badnodes = set(restricted)
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        def dfs(node):
            validchildren = 1
            if node in seen:
                return 0
            seen.add(node)
            if node in badnodes:
                return 0
            for child in graph[node]:
                validchildren += dfs(child)
            return validchildren
                
        seen = set()
        return dfs(0)