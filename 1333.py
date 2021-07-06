# 1333. Filter Restaurants by Vegan-Friendly, Price and Distance
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = []
        
        for id_r, rating_r, veganFriendly_r, price_r, distance_r in restaurants:
            
            if veganFriendly == 1 and veganFriendly_r == 0:
                continue
            
            if distance_r > maxDistance:
                continue
        
            if price_r > maxPrice:
                continue
            
            filtered.append([rating_r, id_r])
        
        filtered.sort(reverse=True)
        return [x[1] for x in filtered]
