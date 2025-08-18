class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        max_profit = 0
        max_price = prices[-1]
        for i in range(l-2, -1, -1):
            max_price = max(max_price, prices[i])


            profit = max_price - prices[i]
            if profit > max_profit:
                max_profit = profit
            
        return max_profit