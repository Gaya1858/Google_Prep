from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) > 2:
            heapq.heapify(stones)
            large = heapq.nlargest(2, stones)
            print(large[0], large[1])
            small = heapq.nsmallest(len(stones) - 2, stones)
            print(large, small)
            check = True
            while check:
                if large[0] != large[1]:
                    small.append(large[0] - large[1])
                    if len(small) > 1:
                        large = heapq.nlargest(2, small)
                        small = heapq.nsmallest(len(small) - 2, small)
                    else:
                        check = False
                else:
                    if len(small) > 1:
                        large = heapq.nlargest(2, small)
                        small = heapq.nsmallest(len(small) - 2, small)
                    else:
                        check = False

            return small[0] if small else 0
        elif len(stones) == 2:
            return abs(stones[0] - stones[1])

        return stones[0]


s = Solution()
print(s.lastStoneWeight(
    [9, 3, 2, 10]))
