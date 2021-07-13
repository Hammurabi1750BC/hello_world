# 162. Find Peak Element

    def findPeakElement(self, nums: List[int]) -> int:
        
        # return nums.index(max(nums))

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
