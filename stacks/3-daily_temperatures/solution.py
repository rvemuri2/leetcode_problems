from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[r]:
                l = stack.pop()
                answer[l] = r-l

            stack.append(r)

        return answer