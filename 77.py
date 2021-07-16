# 77	Combinations

    def combine(self, n: int, k: int) -> List[List[int]]:
        def recurse2combo(nums2date):
            if len(nums2date) == k:
                combos.append(nums2date)    
            else:
                prev = nums2date[-1] if len(nums2date) > 0 else 0
                if len(nums2date) + n+1 - prev+1 >= k:
                    for i in range(prev+1, n+1):
                        recurse2combo(nums2date + [i])
            
        
        combos = []
        recurse2combo([])
        
        return combos
