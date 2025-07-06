class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])

        if len(word1) > min_len:
            result.extend(word1[min_len:])
        elif len(word2) > min_len:
            result.extend(word2[min_len:])

        return ''.join(result)

n=input().lower()
m=input().lower()
s=Solution()
print(s.mergeAlternately(n,m))