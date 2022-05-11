from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy, maxSell = float("inf"), 0
        for price in range(len(prices)):
            minBuy = min(minBuy, prices[price])
            maxSell = max(maxSell, prices[price] - minBuy)

        return maxSell
s =Solution()
print(s.maxProfit([2,4,1]))
