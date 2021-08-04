# 1094. Car Pooling

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickups = []
        for pas, st, end in trips:
            pickups += [[st, pas], [end, -pas]]
        pickups.sort()
        
        in_car = 0
        for location, pas in pickups:
            in_car += pas
            if in_car > capacity:
                return False
        
        return True
