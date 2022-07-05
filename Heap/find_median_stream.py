
import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []



    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap,-1 * num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if self.maxHeap and self.minHeap and (-1 * self.minHeap[0] > self.maxHeap[0]) :
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)

    def findMedian(self) -> float:

        if len(self.minHeap) - len(self.maxHeap) == 1:
            return -1 * self.minHeap[0]
        elif len(self.maxHeap) - len(self.minHeap) == 0:
            return ((-1 * self.minHeap[0]) + (self.maxHeap[0])) / 2
        elif len(self.maxHeap) - len(self.minHeap) == 1:
            return self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
m = MedianFinder()
m.addNum(1)
print(m.findMedian())
m.addNum(2)
print(m.findMedian())
m.addNum(3)
print(m.findMedian())
# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]