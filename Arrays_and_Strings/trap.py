from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        maxl, maxr, area, l, r = height[0], height[len(height)-1], 0, 0, len(height)-1
        while l < r:
            if height[l] <= height[r]:
                if height[l] > maxl:
                    maxl = height[l]
                else:
                    area += (maxl - height[l])
                l += 1
            else:
                if height[r] > maxr:
                    maxr = height[r]
                else:
                    area += (maxr - height[r])
                r -= 1
        return area

s =Solution()
n = [4,2,0,3,2,5]
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap(n))
