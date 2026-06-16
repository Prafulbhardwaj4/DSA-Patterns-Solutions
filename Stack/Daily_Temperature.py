"""
Qn.

Given an array temperatures, return an array res where
res[i] is the number of days until a warmer temperature.

If no future warmer day exists, put 0.

This is a monotonic stack problem.
"""

"""
Solution :

We use a decreasing monotonic stack storing indices.

Traverse left to right.

For each i:
- while stack not empty and temperatures[i] > temperatures[stack[-1]]:
    pop index
    res[popped] = i - popped

- push i into stack

Remaining indices in stack stay 0.

TC -> O(n)
SC -> O(n)
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            stack.append(i) 
        return res
    
"""
Aleternate 


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1] - i

            stack.append(i)

        return res
        
"""