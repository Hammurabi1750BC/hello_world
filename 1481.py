# 1481	Least Number of Unique Integers after K Removals

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr = Counter(arr)
        
        d_counts = defaultdict(lambda : 0)
        for num in arr:
            d_counts[arr[num]] += 1
        
        counts = sorted(d_counts.keys())
        
        remove = 0
        remaining = len(arr)
        
        for count in counts:
            if k - remove < count:
                break
            elif k - remove >= count * d_counts[count]:
                remove += count * d_counts[count]
                remaining -= d_counts[count]
            else:
                remainder = k - remove
                remaining -= remainder//count
                break
        
        return remaining
