from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = [0 for i in digits]
        new[-1] = 1
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            a = new[i] + digits[i] + carry
            if a > 9:
                new[i] = 0
                carry = 1
            else:
                new[i] = a
                carry = 0
        if carry == 1:
            new.insert(0,carry)
        print(new)


        return new
s =Solution()
s.plusOne([2,3,1,9,9,0,9,0])