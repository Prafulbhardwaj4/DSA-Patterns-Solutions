"""
Qn. We are given a list, we just need to reverse it's element without createing a new Lit

"""

"""
Solution :

1) We can just use .reverse()

2) We can use stack

first loop -> appending/pushing the List elements into stak

Second Loop -> Popping the elements from stack and updating List(s) elements one by one

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []

        for i in range(len(s)):
            stack.append(s[i])

        for i in range(len(s)):
            s[i] = stack.pop()