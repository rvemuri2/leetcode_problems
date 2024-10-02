class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        p1 = 0
        p2 = 0

        count = 0

        while(p1 < len(s) and p2 < len(t)): 
            
            if(s[p1] == t[p2]): 
                p1+=1
                p2+=1
                count+=1
            else: 
                p2+=1
            
        if(count == len(s)):
            return True
        else:
            return False
