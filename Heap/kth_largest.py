import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        self.kth = k
        while len(self.nums) > self.kth:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.kth:
            heapq.heappop(self.nums)
        return self.nums[0]




s = KthLargest(3, [4, 5, 8, 2])
print(s.add(3))
print(s.add(5))
print(s.add(10))
print(s.add(9))
print(s.add(4))
# print(s.add(5))
# print(s.add(5))
