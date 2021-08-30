# 789	Escape The Ghosts

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        ghost_distance2target = min(abs(target[0] - gx) + abs(target[1] - gy) for gx, gy in ghosts)
        
        your_distance2target = abs(target[0]) + abs(target[1])
        
        return your_distance2target < ghost_distance2target
