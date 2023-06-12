class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                # Calculate profit
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # Update left as the right is smaller now
                left = right
            right += 1

        return max_profit
