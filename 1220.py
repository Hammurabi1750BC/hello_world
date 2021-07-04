# 1220	Count Vowels Permutation

class Solution:
  # v4
      def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

        return (a + e + i + o + u) % (10 ** 9 + 7)
  
  # v3
      def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        
        #               a  e  i  o  u
        last_letters = [1, 1, 1, 1, 1]
        
        cycle = 2
        while cycle <= n:
            next_letters = [0, 0, 0, 0, 0]
            
            next_letters[0] = last_letters[1] + last_letters[2] + last_letters[4]

            next_letters[1] = last_letters[0] + last_letters[2]

            next_letters[2] = last_letters[1] + last_letters[3]            
            
            next_letters[3] = last_letters[2]
            
            next_letters[4] = last_letters[2] + last_letters[3]                    
            
            last_letters = next_letters
            
            cycle += 1
        
        return sum(last_letters) % (10**9 + 7)
  
  
  # v2
  
      def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        
        #               a  e  i  o  u
        last_letters = [1, 1, 1, 1, 1]
        
        cycle = 2
        while cycle <= n:
            next_letters = [0, 0, 0, 0, 0]
            
            next_letters[1] += last_letters[0]
            
            next_letters[0] += last_letters[1]
            next_letters[2] += last_letters[1]
            
            next_letters[0] += last_letters[2]
            next_letters[1] += last_letters[2]
            next_letters[3] += last_letters[2]
            next_letters[4] += last_letters[2]
            
            next_letters[2] += last_letters[3]            
            next_letters[4] += last_letters[3]                    
            
            next_letters[0] += last_letters[4]
            
            last_letters = next_letters
            
            cycle += 1
        
        return sum(last_letters) % (10**9 + 7)
  
  
  
  # v1
  
  def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        
        last_letters = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        
        cycle = 2
        while cycle <= n:
            next_letters = defaultdict(lambda: 0)
            
            next_letters['e'] += last_letters['a']
            
            next_letters['a'] += last_letters['e']
            next_letters['i'] += last_letters['e']
            
            next_letters['a'] += last_letters['i']
            next_letters['e'] += last_letters['i']
            next_letters['o'] += last_letters['i']
            next_letters['u'] += last_letters['i']
            
            next_letters['i'] += last_letters['o']            
            next_letters['u'] += last_letters['o']                    
            
            next_letters['a'] += last_letters['u']
            
            last_letters = next_letters
            
            cycle += 1
        
        return sum(last_letters.values()) % (10**9 + 7)
      
      
      
      
