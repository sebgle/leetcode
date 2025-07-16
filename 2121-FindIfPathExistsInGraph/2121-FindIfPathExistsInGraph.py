# Last updated: 7/16/2025, 9:42:01 AM
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for node in edges:
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])
        
        seen = set()
        
        def helper(node, destination):
            if node in seen:
                return
            if node == destination:
                return True
            seen.add(node)
            for child in graph[node]:
                if helper(child, destination):
                    return True
        
        if helper(source, destination):
            return True
        else:
            return False