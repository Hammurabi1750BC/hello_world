# Maximum Number of Occurrences of a Substring

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring_counts = defaultdict(lambda: 0)

        for left in range(len(s) - minSize + 1):
            substring2test = s[left:left + minSize]
            if len(set(substring2test)) <= maxLetters:
                substring_counts[substring2test] += 1

        return max(substring_counts.values()) if substring_counts else 0
