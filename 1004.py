# 1004 Max Consecutive Ones III

class Solution:
    
    # 
        l = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
                
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            
        
        return r-l+1
    
    
    
    # first attempt
    
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k >= len(nums):
            return len(nums)

        longest = left = right = zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                if zero_count > k:
                    longest = max(longest, right - left)  # right is a 0 so don't include it

                    while left < right and nums[left] != 0:
                        left += 1
                    left += 1  # left skipped 1 zero
                    zero_count -= 1

                    # if a desert of 0s then ...
                    if left == right:
                        while right < len(nums) and nums[right] == 0:
                            right += 1
                        left = right - k + 1  # can have k zeros total, need room for 1 more zero
                        zero_count = k - 1


        longest = max(longest, right - left + 1)

        return longest
