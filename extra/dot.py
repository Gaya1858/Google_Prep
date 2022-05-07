from collections import Counter, defaultdict
from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = Counter(s)
        print(d)
        for i in t:
            if i not in d or d[i] == 0:
                return False
            else :
                d[i] -= 1
        return True

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumset = set( )

        for i, num in enumerate(nums):
            rem = target - num
            if rem in sumset:
                inde = nums.index(rem)
                return [inde,i]

            else:
                sumset.add(num)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


s =Solution()
print([0]* 26)
print(s.groupAnagrams(strs = ["eats","stea","teas","seta","nat","bat"]))