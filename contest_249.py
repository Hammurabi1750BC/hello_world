# 1929. Concatenation of Array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
        
# 1930. Unique Length-3 Palindromic Subsequences

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pal3s = 0
        
        dlets = defaultdict(list)
        for i, char in enumerate(s):
            dlets[char].append(i)
        
        for char in dlets.keys():
            left = min(dlets[char])
            right = max(dlets[char])
            
            between = set(s[left+1:right])
            pal3s += len(between)
                        
        return pal3s
