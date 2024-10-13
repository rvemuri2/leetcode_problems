class Solution:
    def isValid(self, s: str) -> bool:

        h = {")": "(", "}": "{", "]": "["}

        arr = []

        for i in s:

            if(i == "(" or i == "{" or i == "["):
                arr.append(i)
            
            if(i in h):
                if(len(arr) == 0):
                    return False
                elif(arr[-1] == h[i]):
                    arr.pop()
                else:
                    return False
            
        
        if(len(arr) > 0):
            return False
        else:
            return True