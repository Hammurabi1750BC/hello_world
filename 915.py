# 915. Partition Array into Disjoint Intervals

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        right_start = 1
        
        left_max = max2date = nums[0]
        for i, n in enumerate(nums):
            if n < left_max:
                left_max = max2date
                right_start = i + 1                
            else:
                max2date = max(max2date, n)
        
        return right_start
