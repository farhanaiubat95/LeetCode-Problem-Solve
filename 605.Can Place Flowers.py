from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int):
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (flowerbed[i-1]==0 or i==0) and (flowerbed[i+1]==0 or i==len(flowerbed)-1):
                n-=1
                flowerbed[i]=1
        return n<=0

s=Solution()
print(s.canPlaceFlowers([1,0,0,0,1],2))