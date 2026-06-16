"""
Qn. We will be given a string of parentheses, we need to check whether that string is valid or not 

"""

"""
A string is valid if:
- Every opening bracket has a corresponding closing bracket
- Brackets are closed in the correct order

Types of brackets:
( )
{ }
[ ]

"""

"""
Example : ([]) -> True

          ([)] -> False

          {[]} -> True

          (( -> False

"""

"""
Solution :

This is a Stack problem.

We use stack because:
- It follows LIFO (Last In First Out)
- The last opened bracket must be closed first

Idea :

We traverse the string character by character.

If we see an opening bracket:
    we push it into the stack

If we see a closing bracket:
    we check whether it matches the last opened bracket

We maintain a mapping:

closeToOpen = {
    ")" : "(",
    "}" : "{",
    "]" : "["
}

So for every closing bracket,
we expect a specific opening bracket on top of stack.

Steps :

1) Initialize empty stack

2) Traverse string:

   Case 1: opening bracket
       push into stack

   Case 2: closing bracket
       - check if stack is not empty
       - check top of stack matches expected opening bracket
       - if yes -> pop
       - else -> invalid string, return False

3) After traversal:

   If stack is empty -> all brackets matched -> valid
   If stack is not empty -> unmatched opening brackets -> invalid

Why this works :

- Stack always stores unmatched opening brackets
- Most recent opening bracket must match first closing bracket
- Ensures correct nesting order

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"]":"[",
                       "}":"{",
                       ")":"("
                       }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False