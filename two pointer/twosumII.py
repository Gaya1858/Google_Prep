from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set( )

        for i in range(len(numbers)):
            rem = target - numbers[i]
            if rem not in seen:
                seen.add(numbers[i])
            else:
                ind = numbers.index(rem)
                return [ind, i]
s =Solution()
print(s.twoSum([2,7,11,15],9))