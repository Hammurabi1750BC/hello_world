class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right, l2d):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            left += 1       # last iteration failed
            right -= 1

            if right + 1 - left > len(l2d):
                l2d = s[left:right+1]

            return l2d, right

        l2d = s[0]  # longest pal to date

        for i in range(len(s)):
            for right in [i+1, i+2]:    # aa  aba
                if right < len(s) and s[i] == s[right]:
                    l2d, right = expand(i, right, l2d)
                    if right >= len(s) - 1:
                        return l2d

        return l2d
