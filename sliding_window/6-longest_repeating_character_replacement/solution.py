class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        h = {}
        res = 0

        for i in range(len(s)):

            h[s[i]] = h.get(s[i], 0) + 1

            if((i - l + 1) - max(h.values()) > k):
                h[s[l]] = h.get(s[l]) - 1
                l += 1 
                
            res = max(res, i - l + 1)
        
        return res