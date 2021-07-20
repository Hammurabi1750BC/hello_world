# 384. Shuffle an Array

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        
        rnums = [x for x in self.nums]
        for i in range(len(rnums)):
            swap_dex = random.randint(i, len(rnums)-1)
            rnums[i], rnums[swap_dex] = rnums[swap_dex], rnums[i]
        
        return rnums
        # return random.sample(self.nums, k=len(self.nums))
        
