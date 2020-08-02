class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        l = len(S)
        lst = list(S)
        res = []
        def dfs(n):
            if n == l:
                res.append(''.join(lst))
                return
            dfs(n+1)
            if lst[n].isalpha():
                lst[n]=lst[n].swapcase()
                dfs(n+1)
        dfs(0)
        return res