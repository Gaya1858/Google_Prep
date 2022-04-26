# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []
        re_list = []
        nums.sort( )
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                low = i + 1
                high = len(nums) - 1
                sums = 0 - nums[i]
                while low < high:
                    if nums[low] + nums[high] == sums:
                        re_list.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]: low += 1
                        while low < high and nums[high] == nums[high - 1]: high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] > sums:
                        high -= 1
                    else:
                        low += 1
        return re_list


s = Solution( )
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))
