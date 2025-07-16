# Last updated: 7/16/2025, 9:42:02 AM
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-stone for stone in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            pop = abs(heapq.heappop(piles))
            heapq.heappush(piles, -ceil(pop / 2))
            
        total = 0
        while piles:
            total += abs(heapq.heappop(piles))
            
        return total
            
            
        
        