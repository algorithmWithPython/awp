class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, l, r):
            if l==r==n:
                res.append(str(s))
                return
            if l<n:
                s+="("
                dfs(s, l+1, r)
                s=s[:-1]
            if r<l:
                s+=")"
                dfs(s, l, r+1)
                s=s[:-1]
        
        dfs('', 0, 0)
        return res