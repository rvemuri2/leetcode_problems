class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        count2 = 0

        h = set()

        for i in range(len(s)):

            while(s[i] in h):
                h.remove(s[l])
                l+=1
            count2 = max(count2, i-l + 1)
    
            h.add(s[i])
        
        return count2