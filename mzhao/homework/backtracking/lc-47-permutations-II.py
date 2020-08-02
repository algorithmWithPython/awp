class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        m = {}
        for i in nums:
            m[i] = m.setdefault(i, 0) + 1
        res = []
        
        def calcu(current_map, current_list):
            if not current_map:
                res.append(list(current_list))
                return
            
            key_lst = list(current_map.keys())
            for k in key_lst:
                current_list.append(k)
                if current_map[k] > 1:
                    current_map[k] -= 1
                else:
                    current_map.pop(k)
                calcu(current_map, current_list)
                current_list.pop()
                current_map[k] = m.setdefault(k, 0) + 1
                
        calcu(m, [])
        return res