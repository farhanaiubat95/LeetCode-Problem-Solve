from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int):
        max_candies = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                candies[i]=True
            else:
                candies[i]=False
        return candies
    

s=Solution()
print(s.kidsWithCandies([12,1,12],10))