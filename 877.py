# 877	Stone Game

class Solution:
    
    # v3 turns out it's always True
    def stoneGame(self, piles: List[int]) -> bool:
      return True   

    # v2 
    def stoneGame(self, piles: List[int]) -> bool:

      heap = [[0, piles]]

      while heap:
          score, remainder = heapq.heappop(heap)

          if not remainder:
              if score < 0:
                  return True
          else:
              score_r = remainder[0]
              score_l = remainder[-1]
              remainder_r = remainder[1:]
              remainder_l = remainder[:-1]

              if len(remainder) % 2 == 0:   # track turn using length of piles
                  next_score_l = score - score_l
                  next_score_r = score - score_r
              else:
                  next_score_l = score + score_l
                  next_score_l = score + score_r

              heapq.heappush(heap, [next_score_l, remainder_l])
              heapq.heappush(heap, [next_score_r, remainder_r])

      return False

  
  
  
  
  # v1
    def stoneGame(self, piles: List[int]) -> bool:
        heap = [[0, piles, 1]]
        
        while heap:
            score, remainder, a_turn = heapq.heappop(heap)
        
            if not remainder:
                if score < 0:
                    return True
            else:
                score_r = remainder[0]
                score_l = remainder[-1]
                remainder_r = remainder[1:]
                remainder_l = remainder[:-1]

                if a_turn:
                    next_score_l = score - score_l
                    next_score_r = score - score_r
                else:
                    next_score_l = score + score_l
                    next_score_l = score + score_r
                
                heapq.heappush(heap, [next_score_l, remainder_l, 1-a_turn])
                heapq.heappush(heap, [next_score_r, remainder_r, 1-a_turn])
        
        return False
