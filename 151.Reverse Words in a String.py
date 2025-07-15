class Solution:
    def reverseWords(self, s: str):
        return " ".join(reversed(s.strip().split()))
    
s=Solution()
print(s.reverseWords("a good   example"))