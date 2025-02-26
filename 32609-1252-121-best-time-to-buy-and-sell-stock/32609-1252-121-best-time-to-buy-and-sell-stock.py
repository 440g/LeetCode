class Solution(object):
    def maxProfit(self, prices):
        buy = prices.pop(0)
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy
        return profit

        