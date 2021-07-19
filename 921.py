# 921	Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lefts = min2add = 0
        for char in s:
            if char == '(':
                lefts += 1
            else:
                if lefts > 0:
                    lefts -= 1
                else:
                    min2add += 1
            
        min2add += lefts   # lefts with no rights after
            
        return min2add
