class Solution:
    d = {}
    def myPow(self, x: float, n: int) -> float:
        def iter(x, n):
            ans = 1
            count = n
            prod = x
            while count > 0:
                if count % 2 == 1:
                    ans = ans * prod
                prod = prod * prod
                count = count//2
            return ans

        def fastPow(x, n):
            if n == 0:
                return 1

            half = fastPow(x, n//2)

            if(n %2 == 0):
                return half * half
            else:
                return half * half * x
        if n < 0:
            x = 1/x
            n = -n
        return iter(x, n)








s =Solution()
print(s.myPow(2.000, 6))