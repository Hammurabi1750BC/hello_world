# 1583	Count Unhappy Friends
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        unhappy = 0
        
        d_pairs = dict()
        for fx, fy in pairs:
            d_pairs[fx] = fy
            d_pairs[fy] = fx
        
        for fx in d_pairs.keys():
            fy = d_pairs[fx]
            fx_pref_fy = preferences[fx].index(fy)
            for fu in preferences[fx][:fx_pref_fy]:
                fx_pref_fu = preferences[fx].index(fu)
                
                if fx_pref_fu < fx_pref_fy:                
                    fu_pref_fx = preferences[fu].index(fx)

                    fv = d_pairs[fu]
                    fu_pref_fv = preferences[fu].index(fv)

                    if fu_pref_fx < fu_pref_fv:
                        unhappy += 1
                        break
                        
        return unhappy
    
