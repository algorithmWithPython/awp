from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        stones = piles
         
        # dp[l][r][who]: the largest number of (stones with Alex - stones with Lee)
        # @lru_cache(None)
        # def calcu(l, r, who):
        #     if l>r:
        #         return 0
        #     if who=="A":
        #         return max(stones[l]+calcu(l+1,r,"L"), stones[r]+calcu(l, r-1, "L"))
        #     else:
        #         return min(-stones[l]+calcu(l+1,r,"A"), -stones[r]+calcu(l, r-1, "A"))

        @lru_cache(None)
        # for the person who take stone from [l,r], how many more stones
        # he can have than the other people going to take
        # dp[l][r]: for the current turn, the largest number of (stones of the person taking turn - stones of the other person)
        def calcu(l, r): 
            if l>r:
                return 0
            return max( stones[l]-calcu(l+1, r), stones[r]-calcu(l, r-1) )

        res = calcu(0, len(stones)-1)
        if res>0:
            return True
        else:
            return False

    # dp
    def stoneGame(self, p):
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n): dp[i][i] = p[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0

    # reduced space complexity
    def stoneGame(self, p):
    n = len(p)
    dp = p[:]
    for d in range(1, n):
        for i in range(n - d):
            dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
    return dp[0] > 0    