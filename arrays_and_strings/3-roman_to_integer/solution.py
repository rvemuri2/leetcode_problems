class Solution:
    def romanToInt(self, s: str) -> int:

        map1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum1 = 0
        i = 0

        while(i < len(s)):

            if(i < len(s) - 1 and map1[s[i]] < map1[s[i+1]]):
                sum1 += (map1[s[i+1]] - map1[s[i]])
                i+=2
            else:
                sum1 += map1[s[i]]
                i+=1
                      
        return sum1