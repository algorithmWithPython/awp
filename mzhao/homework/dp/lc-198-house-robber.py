class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        dp = [0]*(n+1)
        dp[0]=0
        dp[1]=nums[0]
        res = dp[1]
        for i in range(2,n+1):
            dp[i] = max(dp[i-1], nums[i-1]+dp[i-2])
        return dp[n]
