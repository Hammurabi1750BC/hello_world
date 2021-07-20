# 398. Random Pick Index

class Solution:

    def __init__(self, nums: List[int]):
        self.dnums = defaultdict(list)
        for i, n in enumerate(nums):
            self.dnums[n].append(i)
            

    def pick(self, target: int) -> int:
        indices = self.dnums[target]
        rand_dex = random.randint(0, len(indices) -1)
        return indices[rand_dex]
        
