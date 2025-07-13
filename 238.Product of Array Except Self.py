from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]):
        n=len(nums)
        result= [1]*n
        
        left=1
        for i in range(n):
            result[i]=left
            left*=nums[i]
        
        right=1
        for i in range(n-1,-1,-1):
            result[i]*=right
            right*=nums[i]

        return result


s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))