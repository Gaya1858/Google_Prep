# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
#
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#
# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
from typing import List
from collections import defaultdict,deque

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        q = deque()
        dd = defaultdict(int)
        res = 0
        for i in fruits:
            q.append(i)
            dd[i] += 1
            while q and len(dd) >2:
                rm =q.popleft()
                dd[rm] -= 1
                if dd[rm] == 0:
                    del dd[rm]
            res = max(res, len(q))


        return res

s = Solution()
print(s.totalFruit([0,1,0,2]))
