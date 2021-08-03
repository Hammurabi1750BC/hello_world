# 90	Subsets II

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        combos = [[]]
        
        for n in nums:
            add2combos = []
            for c in combos:
                add2combos.append(sorted(c + [n]))
            for add2 in add2combos:
                if add2 not in combos:
                    combos.append(add2)
        
        return combos
