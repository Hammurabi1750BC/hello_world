# 524. Longest Word in Dictionary through Deleting
class Solution:

# v2
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:        
        # sort by len, and by first letter
        dictionary.sort(key=lambda x: (-len(x), x) )
        
        for candidate in dictionary:
            dex = 0
            for i in range(len(s)):
                if s[i] == candidate[dex]:
                    dex += 1
                    if dex == len(candidate):
                        return candidate
            
        return ''
        
 # v1
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dd = defaultdict(list)
        for word in dictionary:
            dd[len(word)].append(word)

        lens = sorted(dd.keys(), reverse=True)
        for l in lens:
            matched = []
            for candidate in dd[l]:
                dex = 0
                for i in range(len(s)):
                    x = s[i]
                    y = candidate[dex]

                    if s[i] == candidate[dex]:
                        dex += 1
                        if dex == len(candidate):
                            matched.append(candidate)
                            break

            if matched:
                return sorted(matched)[0]

        return ''
