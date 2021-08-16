# 1006	Clumsy Factorial

class Solution:
    def clumsy(self, n: int) -> int:
        ops = ['*', '/', '+', '-']
        opx = 0
        ans = n
        n -= 1
        total = 0
        
        pieces = []
        
        while n > 0:
            if ops[opx] == '*':
                ans *= n
            elif ops[opx] == '/':
                ans //= n
            elif ops[opx] == '+':
                total += n
            elif ops[opx] == '-':
                pieces.append(ans)
                ans = n
            
            n -= 1
            opx += 1
            if opx > 3:
                opx = 0
        
        pieces.append(ans)
        
        total += pieces[0] 
        if len(pieces) > 0:
            total -= sum(pieces[1:])
            
        return total
