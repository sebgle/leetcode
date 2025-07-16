# Last updated: 7/16/2025, 9:42:46 AM
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        curr = startGene
        mutations = ['A', 'C', 'G', 'T']
        queue = deque([(curr, 0)])
        seen = {curr}
        
        while queue:
            curr, steps = queue.popleft()
            print(curr, steps)
            if curr == endGene:
                return steps
            temp = list(curr)
            for i in range(len(temp)):
                original = temp[i]
                for mutation in mutations:
                    temp[i] = mutation
                    mutated = ''.join(temp)
                    if mutated in bank and mutated not in seen:
                        queue.append((mutated, steps + 1))
                        seen.add(mutated)
                temp[i] = original
        
        return -1
        
        