class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = prices[0]

        for p in prices:
            maxP = max(maxP, p - minP)
            minP = min(minP, p)

        return maxP