class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        p = [0]*10
        res = []
        def add_time():
            h, m =0,0
            for i in range(4):
                if p[i]:
                    h += 2**i
            for i in range(6):
                if p[i+4]:
                    m += 2**i
            if h<12 and m<60:
                res.append(f'{h}:{m:0>2}')
            
        def dfs(i, n):
            if i==10:
                if n==num:
                    add_time()
                return
            
            if n==num:
                add_time()
                return
            
            p[i]=1
            dfs(i+1, n+1)
            p[i]=0
            dfs(i+1, n)
            
        dfs(0, 0)
        return res