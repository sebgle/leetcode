# Last updated: 7/16/2025, 9:42:22 AM
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heapq.heapify(sticks)
        
        def helper(total):
            if len(sticks) < 2:
                return 0
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            total = stick1 + stick2
            heapq.heappush(sticks, total)
            return total + helper(total)
    
        return helper(0)
        
        