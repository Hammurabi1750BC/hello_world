#1679. Max Number of K-Sum Pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) -1
        
        ops = 0
        
        while left < right:
            if nums[left] > k/2:
                break
            
            this_sum = nums[left] + nums[right]
            if this_sum == k:
                ops += 1
                left += 1
                right -= 1
            elif this_sum < k:
                left += 1
            else:
                right -= 1
        
        return ops
