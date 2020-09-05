from functools import lru_cache
class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     @lru_cache(maxsize=None)
    #     def splittable(i):
    #         if i == len(s):
    #             return True
    #         for j in range(i, len(s)):
    #             if s[i:j+1] in wordDict:
    #                 res = splittable(j+1)
    #                 if res == True:
    #                     return True
    #         return False
    #     return splittable(0)
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        slen = len(s)
        dp = [False]*(slen+1)
        dp[0]=True
        for i in range(1, slen+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[slen]