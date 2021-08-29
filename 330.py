# 330. Patching Array

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        min_patches = reached = num_dex = 0
        
        while reached < n:
            if num_dex < len(nums) and reached >= nums[num_dex] - 1:
                reached += nums[num_dex]
                num_dex += 1
            else:
                min_patches += 1
                reached += reached + 1                       
        
        return min_patches
