# Last updated: 7/16/2025, 9:42:57 AM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
            
        return nums[0]
        