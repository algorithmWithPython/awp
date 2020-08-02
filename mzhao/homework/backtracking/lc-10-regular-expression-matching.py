class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl = len(s)
        pl = len(p)
        def match(sp, pp):
            if pp == pl:
                if sp == sl:
                    return True
                return False
            
            if sp == sl:
                if (pl-pp)%2:
                    return False
                for i in range(pp+1, pl, 2):
                    if p[i]!= '*':
                        return False
                return True
            
            if p[pp] == '.':
                if pp+1<pl and p[pp+1]=='*':
                    res = False
                    for i in range(sp, sl+1):
                        res = res or match(i, pp+2)
                    return res
                return match(sp+1, pp+1)
            
            if pp+1<pl and p[pp+1] == '*':
                res = match(sp, pp+2)
                while sp<sl and s[sp] == p[pp]:
                    res = res or match(sp+1, pp+2)
                    sp += 1
                return res
            
            if s[sp] == p[pp]:
                return match(sp+1, pp+1)
            return False
        
        return match(0, 0)
        