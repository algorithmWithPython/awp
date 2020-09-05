class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        max_v = max(nums)
        # dp[i]: the max of sub array having nums[i] as the last element 
        dp = [0]*l
        dp[0] = nums[0]
        for i in range(1, l):
            # dp[i] = nums[i] + if dp[i-1]>0: dp[i-1] else 0
            dp[i] = nums[i] + max(dp[i-1], 0)
            max_v = max(max_v, dp[i])
        return max 

        # which lead to:
        # max_v = max(nums)
        # sum = 0
        # for i in nums:
        #     sum = i + max(sum, 0)
        #     max_v = max(max_v, sum)
        # return max_v
