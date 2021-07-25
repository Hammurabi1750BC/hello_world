# 1493	Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        if 1 not in nums:
            return 0
        
        longest = ones = 0
        
        zero_after_1dex = None
        
        for i, n in enumerate(nums):
            if n == 1:
                ones += 1
                longest = max(longest, ones)
            else:   # n == 0
                if zero_after_1dex != None:
                    ones = i - zero_after_1dex - 1
                zero_after_1dex = i
        
        return longest
