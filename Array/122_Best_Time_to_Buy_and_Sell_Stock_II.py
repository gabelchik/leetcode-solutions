# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#
#         (flag, profit) = (-1, 0)
#         for i in range(len(prices) - 1):
#             if flag == -1:
#                 if prices[i+1] > prices[i]:
#                     flag = i
#                     if prices[i+1] - prices[flag] > 0 :
#                         profit += prices[i+1] - prices[flag]
#                         flag = -1
#             else:
#                 if prices[i + 1] - prices[flag] >= 0:
#                     profit += prices[i + 1] - prices[flag]
#                     flag = -1
#
#         return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
