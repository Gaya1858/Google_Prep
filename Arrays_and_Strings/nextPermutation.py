# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
#
# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
#
# The replacement must be in place and use only constant extra memory.
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:

        ind = 0
        # find the index to start with and break
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                ind = i
                break
        # if the index is 0 then which means we have to reverse the array
        if ind == 0:
            return nums[::-1]
        # if ind != 0 then check if the rest of the value are in
        # lexicographical order
        swap = len(nums) - 1
        while nums[ind -1] >= nums[swap]:
            swap -= 1
        nums[swap], nums[ind-1] = nums[ind-1], nums[swap]

        nums[ind:] = sorted(nums[ind:])
        return nums



    def permutation(self, nums: List[int])-> List[List[int]]:
        result = []
        # base case, assuming that the array length will start from 1
        if len(nums) == 1:
            return [nums.copy()]
        # recursive case
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permutation(nums)

            for perm in perms:
                perm.append(n)
            nums.append(n)
            result.extend(perms)
        return result







s =Solution()
nums = [1,3,5,4,3,2,1]
print(s.nextPermutation(nums))
nums = [8,0,2,5,6,1]
print(s.nextPermutation(nums))
nums = [1,2,3]
#print(s.permutation(nums))