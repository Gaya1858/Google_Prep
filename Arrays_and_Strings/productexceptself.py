from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(1, len(nums)):
            ans.append(ans[-1] * nums[i-1])
        right  = 1
        for j in range(len(nums)-1, -1, -1):
            ans[j] = ans[j] * right
            right *= nums[j]
        return ans
        # prefix = [nums[0]]
        # suffix = [nums[-1]]
        # length = len(nums) -2
        # for i in range(1, len(nums)):
        #     prefix.append(prefix[-1]*nums[i])
        #     suffix.append(suffix[-1]* nums[length])
        #     length -= 1
        # suffix = list(reversed(suffix))
        # length += 1
        # while length < len(nums):
        #     if length == 0:
        #         nums[length] = suffix[length+1]
        #     elif length == len(nums)-1:
        #         nums[length] = prefix[length -1]
        #     else:
        #         nums[length] = prefix[length-1] * suffix[length + 1]
        #     length += 1
        # return nums
s =Solution()
print(s.productExceptSelf(nums = [1,2,3,4]))


