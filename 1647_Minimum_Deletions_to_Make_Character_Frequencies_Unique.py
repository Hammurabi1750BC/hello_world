class Solution:
    def minDeletions(self, s: str) -> int:
        min_dels = 0
        s = Counter(s)
        tallies = set()
        
        for char, tally in s.items():
            while tally > 0 and tally in tallies:
                min_dels += 1
                tally -= 1
            if tally > 0:
                tallies.add(tally)
                    
        return min_dels
    
    
    
    def minDeletions_first_attempt(self, s: str) -> int:
        min_dels = 0
        s = Counter(s)
        tallies = set()
        d_same_freq = defaultdict(lambda: 1)  # if you have a match, start at 2
        
        for char in s.keys():
            tally = s[char]
            if tally in tallies:
                d_same_freq[tally] += 1
            tallies.add(tally)
        
        for tally in d_same_freq.keys():
            instances2move = d_same_freq[tally]
            while instances2move > 1:
                next_available = max(set(range(tally)).difference(tallies))
                min_dels += tally - next_available
                if next_available > 0:
                    tallies.add(next_available)
                instances2move -= 1
                    
        return min_dels
    
