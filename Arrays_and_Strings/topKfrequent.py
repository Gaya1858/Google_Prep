import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)

        ans = {k: v for k, v in sorted(d.items( ), key=lambda item: item[1],reverse=True)}
        re = []
        co = 0
        for i in ans:
            re.append(i)
            co += 1
            if co == k:
                break

        return re

s =Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))