class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force sol
        res = 0
        n = len(prices)

        for i in range(n):
            for j in range(i, n):
                res = max(res, prices[j] - prices[i])


        return res
            