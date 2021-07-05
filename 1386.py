#


# v2

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        group4s = 0
        
        dres = defaultdict(set)
        # 1 = 2 or 3 seat taken
        # 2 = 4 or 5
        # 3 = 6 or 7
        # 4 = 8 or 9
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 3:
                dres[row].add(1)
            elif 4 <= seat <= 5:
                dres[row].add(2)
            elif 6 <= seat <= 7:
                dres[row].add(3)
            elif 8 <= seat <= 9:
                dres[row].add(4)
            
        for row in dres.keys():
            if 1 not in dres[row] and 2 not in dres[row]:
                if 3 not in dres[row] and 4 not in dres[row]:
                    group4s += 2
                else:
                    group4s += 1
            elif 2 not in dres[row] and 3 not in dres[row]:
                group4s += 1
            elif 3 not in dres[row] and 4 not in dres[row]:
                group4s += 1
                            
        empty_rows = n - len(dres.keys())
        group4s += empty_rows * 2
        
        return group4s
      
      
      
    # v1
    
    class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        group4s = 0
        
        dres = defaultdict(set)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:      # ignore extremes        
                dres[row].add(seat)
            
        left = set([2, 3, 4, 5])
        middle = set([4, 5, 6, 7])
        right = set([6, 7, 8, 9])
            
        for row in dres.keys():
            remainder = set(range(2,10)).difference(set(dres[row]))
            
            left_open = len(left.intersection(remainder))
            mid_open = len(middle.intersection(remainder))            
            right_open = len(right.intersection(remainder))
            
            if left_open == 4 or right_open == 4 or mid_open == 4:
                group4s += 1
                if left_open == 4 and right_open == 4:
                    group4s += 2
                
        
        empty_rows = n - len(dres.keys())
        group4s += empty_rows * 2
        
        return group4s
