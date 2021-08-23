class Solution:
    def maxProfit(prices):

        profit = 0
        for i in range(1, len(prices)):
            if(prices[i] > prices[i-1]):
                profit += prices[i] - prices[i-1]

        return(profit)


# # Test solutions
#     print(maxProfit(prices=[6, 1, 3, 2, 4, 7]))
#     print(maxProfit(prices=[1, 2, 3, 4, 5]))
#     print(maxProfit(prices=[7, 6, 4, 3, 1, 9]))
#     print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
