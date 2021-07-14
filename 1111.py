# 1111	Maximum Nesting Depth of Two Valid Parentheses Strings

# v2
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ab_list = []
        
        lefts = 0
        for char in seq:
            if char == '(':
                ab_list.append(lefts %2)
                lefts += 1
            else:
                lefts -= 1
                ab_list.append(lefts %2)
        
        return ab_list

  # v1
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ab_list = []
        
        lefts = 0
        for char in seq:
            if char == '(':
                if lefts %2 == 0:
                    ab_list.append(0)
                else:
                    ab_list.append(1)
                lefts += 1
            else:
                if char == ')':
                    lefts -= 1
                if lefts %2 == 0:
                    ab_list.append(0)
                else:
                    ab_list.append(1)
        
        return ab_list
