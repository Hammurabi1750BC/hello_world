# 49	Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dgrams = defaultdict(list)
        
        for term in strs:
            dgrams[tuple(sorted(term))].append(term)
        
        return dgrams.values()
