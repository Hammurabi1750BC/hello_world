# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[-1] > nums[0]:
            return nums[0]

        left, right = 0, len(nums) - 1

        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
