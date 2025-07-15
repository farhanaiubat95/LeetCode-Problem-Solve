class Solution:
    def reverseVowels(self, s: str):
        vowels =['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        p=[]
        for i in range(len(s)):
            if s[i] in vowels:
                p.append(s[i])
                s[i]='$'
        p.reverse()  

        for i in range(len(s)):
            if s[i]=='$':
                s[i]=p.pop(0) 
                
        return "".join(s)

s=Solution()
print(s.reverseVowels("leetcode"))        