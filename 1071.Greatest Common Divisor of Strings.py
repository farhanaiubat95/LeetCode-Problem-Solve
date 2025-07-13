import math
class Solution:
    def gcdOfStrings(self, str1, str2):
        n= math.gcd(len(str1),len(str2))
        if str1+str2 != str2+str1:
            return ""
        return str1[:n]
    
S=Solution()
print(S.gcdOfStrings("ABABAB","ABAB"))