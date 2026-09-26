class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1:
            return 0

        l = 0
        r = 1
        maxP = 0

        while r < n:
            if prices[r] > prices[l]:
                maxP = max(maxP, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r = l + 1

        return maxP

