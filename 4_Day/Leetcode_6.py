# Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

#Method 1 : Using One Pass Algorithm (Preferred Method)
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
# Explanation : We initialize min_price to the first price and max_profit to 0. We iterate through the prices, updating min_price if we find a lower price. We calculate the profit for each price and update max_profit if the profit is greater than the current max_profit. Finally, we return max_profit.
# Time Complexity : O(n) where n is the number of prices.
# Space Complexity : O(1) as we are using only a constant amount of space.

# Method 2 : Using Kadane's Algorithm (Also works but not as intuitive for this problem)
class Solution(object):
    def maxProfit(self, prices):
        max_current = 0
        max_global = 0
        for i in range(1, len(prices)):
            max_current = max(0, max_current + prices[i] - prices[i - 1])
            if max_current > max_global:
                max_global = max_current
        return max_global
# Explanation : We initialize max_current to 0 and max_global to 0. We iterate through the prices starting from the second price, updating max_current to be the maximum of 0 and the difference between the current price and the previous price. We update max_global if max_current is greater than the current max_global. Finally, we return max_global.
# Time Complexity : O(n) where n is the number of prices.
# Space Complexity : O(1) as we are using only a constant amount of space.


# Method 3 : Using Brute Force (Not recommended due to inefficiency)
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
# Explanation : We use two nested loops to check every possible pair of buy and sell days. We calculate the profit for each pair and update max_profit if the profit is greater than the current max_profit. Finally, we return max_profit.
# Time Complexity : O(n^2) where n is the number of prices.
# Space Complexity : O(1) as we are using only a constant amount of space.