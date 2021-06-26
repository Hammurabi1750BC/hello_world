# 1909_Remove_One_Element_to_Make_the_Array_Strictly_Increasing

def canBeIncreasing(self, nums: List[int]) -> bool:
    for i in range(len(nums)):
        nums2check = nums[:i] + nums[i+1:]
        if nums2check == sorted(nums2check) and len(nums2check) == len(set(nums2check)):
            return True

    return False

# attempt 1
def canBeIncreasing(self, nums: List[int]) -> bool:
    def check4increasing(nums2check):
        for i in range(1, len(nums2check)):
            if nums2check[i-1] >= nums2check[i]:
                return False
        return True

    for i in range(len(nums)):
        nums2check = nums[:i] + nums[i+1:]
        in_order = check4increasing(nums2check)
        if in_order:
            return True

    return False
