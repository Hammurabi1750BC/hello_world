# 1492 The kth Factor of n
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        sq_root = int(math.sqrt(n))
        factors = [1, n]
                
        for i in range(2, sq_root + 1):
            if n % i == 0:
                factors += [i, n // i]
        
        if sq_root * sq_root == n:
            factors.remove(sq_root)
        
        factors.sort()
        return -1 if k - 1 >= len(factors) else factors[k - 1]
