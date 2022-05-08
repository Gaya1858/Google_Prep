from typing import List
import  bisect


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        seen =[]
        for i in reversed(nums):
            x = bisect.bisect_left(seen, i)
            bisect.insort(seen, i)
        counts = 1
        hold = counts
        for i in range(len(seen)-1):
            if seen[i+1] - seen[i] == 1:
                counts += 1
            elif seen[i+1] - seen[i] == 0:
                continue
            else:
                if counts ==1 and seen[i+1] - seen[i] > 1:
                    continue
                else:
                    hold = max(hold, counts)
                    counts = 1


        return max(hold, counts)






s =Solution()
print(s.longestConsecutive(

[9,1,4,7,3,-1,0,5,8,-1,6]))