class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str1 = ""
        p1 = 0
        p2 = 0

        while(p1 < len(word1) and p2 < len(word2)):
            str1 += word1[p1]
            str1 += word2[p2]
        
            p1 += 1
            p2 += 1
        
        if(p1 < len(word1)):
            str1 += word1[p1:]
        if(p2 < len(word2)):
            str1 += word2[p2:]
        
        return str1