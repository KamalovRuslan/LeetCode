import pandas as pd


class Solution(object):
    @classmethod
    def maxProfit(self, k, prices):
        n = len(prices)
        if n < 2:
            return 0
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        glob = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            local = [0] * n
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                local[j] = max(glob[i - 1][j - 1] + profit,
                               glob[i - 1][j - 1],
                               local[j - 1] + profit)
                glob[i][j] = max(glob[i][j - 1], local[j])
        return glob[k][-1]
