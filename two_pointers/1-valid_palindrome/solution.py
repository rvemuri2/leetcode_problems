class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join(char for char in s if char.isalnum())

        l = 0
        r = len(clean_text) - 1

        clean_text= clean_text.lower()

        while(l < r):
            if(clean_text[r] != clean_text[l]):
                return False
            r-=1
            l+=1
        
        return True