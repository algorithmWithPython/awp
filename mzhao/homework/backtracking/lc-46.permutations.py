class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []
        def dfs(p):
            if len(p) == l:
                res.append(list(p))
                return
            for i in range(l):
                if nums[i] not in p:
                    p.append(nums[i])
                    dfs(p)
                    p.pop()
        dfs([])
        return res