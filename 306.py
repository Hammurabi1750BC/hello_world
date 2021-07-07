# 306	Additive Number

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def recurse2sum(num2back, num1back, remainder):
            if remainder == '':
                return False

            sum2test = num2back + num1back
            if sum2test == int(remainder):
                if remainder[0] == '0':
                    return sum2test == 0
                else:
                    return True

            elif sum2test > int(remainder):
                return False

            elif sum2test < int(remainder):
                for i in range(1, len(remainder) + 1):
                    if remainder[0] == '0' and i != 1:
                        break

                    try_num1back = int(remainder[:i])
                    if sum2test < try_num1back:
                        break
                    if sum2test == try_num1back:
                        next_num2back = num1back
                        next_remainder = remainder[i:]
                        next_tf = recurse2sum(next_num2back, try_num1back, next_remainder)
                        if next_tf:
                            return True

            return False

        for i in range(1, len(num) + 1 - 2):
            if num[0] == '0' and i != 1:
                return False

            num2back = int(num[:i])

            for j in range(i + 1, len(num)):
                if num[i] == '0' and j != i + 1:
                    continue

                num1back = int(num[i:j])
                remainder = num[j:]

                if num2back + num1back > int(remainder):
                    break

                if recurse2sum(num2back, num1back, remainder):
                    return True

        return False
