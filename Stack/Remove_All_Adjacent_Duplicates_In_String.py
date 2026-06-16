"""
Qn. We are given a string, we need to delete pairs of duplicates from string

"""

"""
Solution : 

Maintain an answer which we will return, ans = ""
add first element to answer
then come to second element and compare it with recent element of ans

if same drop both
else add second element too

third element, same, compare with recent element of ans,
if same drop third element of string, and second element of ans

and goes on till last element of string

return ans

"""

"""
Example : [abbaca] -> [ca]
          [bbbcdd] -> [bcd]

"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        res = ""

        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue

            if stack[-1] == s[i]:
                stack.pop()
                continue

            stack.append(s[i])
        
        while stack:
            res += stack.pop()
        
        return res[::-1]
    
"""
Alternate Approach

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
"""