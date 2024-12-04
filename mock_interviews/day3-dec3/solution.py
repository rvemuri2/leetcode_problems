from collections import Counter
def longestSubstring(str1, k):

    h = {}

    left = 0
    ans = 0

    for i in range(len(str1)):
        h[str1[i]] = h.get(str1[i], 0) + 1

        if(str1[i] == max(h.values())):
            k -= 1

        while(str1[left] != max(h.values()) and k < 0):
            h[str1[left]] -= 1
            left += 1
            k += 1
        ans = max(ans, left + i + 1)
    
    return ans

print(longestSubstring("ABAB", 2))