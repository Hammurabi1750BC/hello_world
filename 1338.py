# 1338	Reduce Array Size to The Half

class Solution:
  # v2
      def minSetSize(self, arr: List[int]) -> int:
        orig_len = len(arr)
        
        arr = Counter(arr)
        
        counts = sorted(arr.values(), reverse=True)
        
        removed_set_count = removed_total_count = 0
        
        for count in counts:            
            if removed_total_count >= orig_len / 2:
                break
            removed_total_count += count
            removed_set_count += 1
        
        return removed_set_count
  
  # v1 
  
    def minSetSize(self, arr: List[int]) -> int:
        orig_len = arr_len = len(arr)
        
        arr = Counter(arr)
        
        counts = sorted(arr.values(), reverse=True)
        
        removed_set_count = 0
        
        count_dex = 0
        while arr_len > orig_len / 2:
            arr_len -= counts[count_dex]
            count_dex += 1
            removed_set_count += 1
        
        return removed_set_count
