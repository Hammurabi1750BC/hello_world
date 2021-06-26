# 1909_Remove_One_Element_to_Make_the_Array_Strictly_Increasing

# O(n)
def canBeIncreasing(self, nums: List[int]) -> bool:
    last_nix = -1
    count_ni = 0

    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            last_nix = i
            count_ni += 1
            if count_ni > 1:
                return False

    if count_ni == 0:
        return True

    if count_ni == 1:
        if last_nix == 0 or last_nix == len(nums)-2:
            return True
        if nums[last_nix-1] < nums[last_nix+1] or (last_nix+2 < len(nums) and nums[last_nix] < nums[last_nix+2]):
            return True

    return False


# version 2
def canBeIncreasing(self, nums: List[int]) -> bool:
    for i in range(len(nums)):
        nums2check = nums[:i] + nums[i+1:]
        if nums2check == sorted(nums2check) and len(nums2check) == len(set(nums2check)):
            return True

    return False

# version 1
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
