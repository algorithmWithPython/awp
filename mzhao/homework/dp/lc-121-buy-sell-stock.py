class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n= len(prices)
        if n<2:
            return 0
        # dp: the min price to the current day
        dp = [0]*n
        dp[0]=prices[0]
        for i in range(1,n):
            dp[i] = min(dp[i-1], prices[i])
            res = max(res, prices[i]-dp[i-1])
        return res

    # another way, if we can calculate the difference of the two consective days,
    # if change to lc-53, which we have already dealt with. 

    # def maxProfit(self, prices: List[int]) -> int:
    #     RES = 0
    #     maxCur = 0
    #     for i in range(len(prices):
    #         maxCur = max(0, maxCur + prices[i] - prices[i-1])
    #         res = max(maxCur, res)
    #     }
    #     return res;
    # }