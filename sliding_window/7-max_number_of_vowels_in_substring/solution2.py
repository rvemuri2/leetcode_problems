class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        res = 0
        a = ["a", "e", "i", "o", "u"]
        count = 0

        for i in range(len(s)):

            if(s[i] in a):
                count += 1

            if(i - l + 1 == k):
                res = max(res, count)
                if(s[l] in a):
                    count -= 1
                
                l += 1
        return res