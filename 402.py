# 402. Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if num == '0' or k >= len(num):
            return '0'

        stack = []

        i = 0
        while i < len(num) and k > 0:
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1

            stack.append(num[i])
            i += 1

        filtered_num = ''.join(stack)

        if i == len(num) and k > 0:
            filtered_num = filtered_num[:-k]
        elif i < len(num):
            filtered_num += num[i:]

        if filtered_num == '':
            return '0'
        return str(int(filtered_num))       # strip leading zeros
