class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(0,len(prices)-1):
        #     for j in range(i+1,(len(prices))):
        #         profit = (prices[j] - prices[i])
        #         if i!=j and profit >= max_profit:
        #             max_profit = profit

        # return max_profit
        max_profit = 0
        min_price_till_now = float('inf') # show positive infinity
        for i in range(0,len(prices)):
            if prices[i] - min_price_till_now > max_profit:
                max_profit = prices[i] - min_price_till_now
            if prices[i] < min_price_till_now:
                min_price_till_now = prices[i]
        
        return max_profit

