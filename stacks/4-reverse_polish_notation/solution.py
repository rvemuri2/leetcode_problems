from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        nums = []

        for i in tokens:
            if(i == "+" or i == "*" or i == "-" or i == "/"):
                num1 = nums.pop()
                num2 = nums.pop()
                if(i == "+"):
                    res = num1 + num2
                    nums.append(res)
                elif(i == "-"):
                    res = num2 - num1
                    nums.append(res)
                elif(i == "*"):
                    res = num1 * num2
                    nums.append(res)
                elif(i == "/"):
                    res = int(num2 / num1)
                    nums.append(res)
            else:
                nums.append(int(i))
        return nums[0]