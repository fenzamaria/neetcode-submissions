class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1,len(prices)):
            sell = prices[i]
            buy = min(prices[:i])
            profit = sell-buy
            if(profit> maxProfit):
                maxProfit= profit
        return maxProfit
            