# Last updated: 7/16/2025, 9:42:14 AM
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        seen = set()
        
        def validMove(index, move):
            return 0 <= index + move < len(arr) and index + move not in seen
        
        def dfs(index):
            if arr[index] == 0:
                return True
            if validMove(index, arr[index]) and validMove(index, -arr[index]):
                seen.add(index + arr[index])
                seen.add(index - arr[index])
                return dfs(index + arr[index]) or dfs(index - arr[index])
            elif validMove(index, arr[index]):
                seen.add(index + arr[index])
                return dfs(index + arr[index])
            elif validMove(index, -arr[index]):
                seen.add(index - arr[index])
                return dfs(index - arr[index])
            else:
                return False
            
        return dfs(start)
            
            
        