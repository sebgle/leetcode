# Last updated: 7/16/2025, 9:42:28 AM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x,y):
            return sqrt((0-x)**2 + (0-y)**2)
        
        spoints = []
        graph = defaultdict(list)
        heapq.heapify(spoints)
        
        for point in points:
            dist = distance(point[0], point[1])
            graph[dist].append(point)
            heapq.heappush(spoints, dist)
        
        ans = []
        for _ in range(k):
            dist = heapq.heappop(spoints)
            for points in graph[dist]:
                if len(ans) == k:
                    return ans
                ans.append(points)
                
        return ans
            
        