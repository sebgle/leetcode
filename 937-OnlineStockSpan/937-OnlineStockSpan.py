# Last updated: 7/16/2025, 9:42:31 AM
class StockSpanner:

    def __init__(self):
        self.stack = [] 
        
    def next(self, price: int) -> int:
        ans = 1
        while self.stack and price >= self.stack[-1][0]:
            ans += self.stack.pop()[1]
        self.stack.append([price, ans])
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)