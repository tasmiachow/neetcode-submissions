class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        max_profit = 0

        for R in range(len(prices)):
            if prices[R] > prices[left]:
                max_profit = max((prices[R]-prices[left]), max_profit)
            else: 
                left = R
        return max_profit