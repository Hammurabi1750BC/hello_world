# 209	Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        left = subtotal = 0
        for right in range(len(nums)):
            subtotal += nums[right]
            while subtotal >= target:
                min_len = min(min_len, right - left + 1)
                subtotal -= nums[left]
                left += 1

        return min_len if min_len < len(nums) + 1 else 0
