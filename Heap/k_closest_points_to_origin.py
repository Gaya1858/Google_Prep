import heapq
from typing import List
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # loop through the points and calculate euclidean distance
        # push to heap with the new list as tuples
        minHeap =[]

        for i in points:
            heapq.heappush(minHeap,(math.sqrt((0-i[0])**2 + (0-i[1])**2),i))
        small = [x for i, x in heapq.nsmallest(k,minHeap)]

        return small


s = Solution()
print(s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))