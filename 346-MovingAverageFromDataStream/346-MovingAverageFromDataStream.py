# Last updated: 7/16/2025, 9:42:48 AM
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.sum = 0
        self.maxsize = size

    def next(self, val: int) -> float:
        self.sum += val
        self.queue.append(val)
        while len(self.queue) > self.maxsize:
            self.sum -= self.queue.popleft()
        return self.sum / len(self.queue)
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)