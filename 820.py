# 820	Short Encoding of Words

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        non_overlap_words = set(words)
        
        for word in words:
            for i in range(1, len(word)):
                non_overlap_words.discard(word[i:])
            
        return sum(len(word) + 1 for word in non_overlap_words)
