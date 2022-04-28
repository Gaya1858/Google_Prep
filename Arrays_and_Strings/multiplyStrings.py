# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
# Input: num1 = "2", num2 = "3"
# Output: "6"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        add_result = []
        place_zero = ""
        value = ""
        carry = 0
        for i in reversed(num2):
            for j in reversed(num1):
                n = int(i) * int(j) + carry
                if n > 9:
                    x = n % 10
                    value = str(x) + value
                    carry = n // 10
                else:
                    value = str(n) + value
                    carry = 0

            if carry > 0:
                value = str(carry) + value

            add_result.append(value + place_zero)
            carry = 0
            value = ""
            place_zero = place_zero + "0"
            print(add_result)
        result = str( sum([int(x) for x in add_result]))
        return result


s =Solution()
num1 = "123456789"

num2 = "987654321"
print(s.multiply(num1, num2))