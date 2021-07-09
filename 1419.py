# 1419	Minimum Number of Frogs Croaking

class Solution:
  
  # v2
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
      min_frogs = 0
      d_croaks = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}

      for char in croakOfFrogs:
          d_croaks[char] += 1

          if char == "c":
              min_frogs = max(min_frogs, d_croaks['c'] - d_croaks['k'])

          if not d_croaks['c'] >= d_croaks['r'] >= d_croaks['o'] >= d_croaks['a'] >= d_croaks['k']:
              return -1

      return min_frogs if d_croaks['c'] == d_croaks['k'] else -1
  
  
  # v1
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        min_frogs = 0
        
        d_croaks = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        #                 c  r  o  a  k
        partial_croaks = [0, 0, 0, 0]
        
        for char in croakOfFrogs:
            index = d_croaks[char]
            
            if char != 'c':
                partial_croaks[index-1] -= 1
                if partial_croaks[index-1] < 0:
                    return -1
                
            if char != 'k':
                partial_croaks[index] += 1
                min_frogs = max(min_frogs, sum(partial_croaks))
        
        return min_frogs if sum(partial_croaks) == 0 else -1
    
