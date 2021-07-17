# 927. Three Equal Parts

class Solution:

# v2
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = sum(arr)
        if ones % 3 != 0:
            return [-1, -1]
        if ones == 0:
            return [0, 2]

        s1left = arr.index(1)
        s2left = s3left = -1
        sum2date = 1
        i = s1left + 1
        while i < len(arr):
            sum2date += arr[i]
            if sum2date == ones / 3 + 1 and s2left < 0:
                s2left = i
            elif sum2date == ones * 2 / 3 + 1:
                s3left = i
                break
            i += 1

        slice_len = len(arr[s3left:])  # including any trailing zeros
        if arr[s1left:s1left + slice_len] == arr[s2left:s2left + slice_len] == arr[s3left:]:
            return [s1left + slice_len - 1, s2left + slice_len]
        else:
            return [-1, -1]

# v1
    def threeEqualParts_v1(self, arr: List[int]) -> List[int]:
        def get_enough_1s(left, right):
            sum1 = sum(arr[left:right])

            while sum1 < ones / 3 and right < len(arr):
                sum1 += arr[right]
                right += 1

            return right - 1

        def test_equal_binary(rs1, rs2):
            slice1sum = int(''.join([str(x) for x in arr[0:rs1 + 1]]))
            slice2sum = int(''.join([str(x) for x in arr[rs1 + 1:rs2 + 1]]))
            if slice1sum != slice2sum:
                return False
            slice3sum = int(''.join([str(x) for x in arr[rs2 + 1:]]))
            return slice2sum == slice3sum

        ones = sum(arr)
        if ones % 3 != 0:
            return [-1, -1]
        if ones == 0:
            return [0, 2]

        right_slice1 = get_enough_1s(0, ones // 3)

        right_slice2 = get_enough_1s(right_slice1 + 1, right_slice1 + ones // 3)

        right_slice3 = get_enough_1s(right_slice2 + 1, right_slice2 + ones // 3)

        if right_slice3 == len(arr) - 1:  # no trailing zeros possible
            if test_equal_binary(right_slice1, right_slice2):
                return [right_slice1, right_slice2 + 1]
            else:
                return [-1, -1]
        else:  # trailing zeros required
            trailing_zeros = len(arr) - right_slice3 - 1
            if sum(arr[right_slice1 + 1:right_slice1 + 1 + trailing_zeros]) > 0:
                return [-1, -1]
            if sum(arr[right_slice2 + 1:right_slice2 + 1 + trailing_zeros]) > 0:
                return [-1, -1]
            right_slice1 += trailing_zeros
            right_slice2 += trailing_zeros
            right_slice3 += trailing_zeros
            if test_equal_binary(right_slice1, right_slice2):
                return [right_slice1, right_slice2 + 1]
            else:
                return [-1, -1]

        return [-1, -1]
