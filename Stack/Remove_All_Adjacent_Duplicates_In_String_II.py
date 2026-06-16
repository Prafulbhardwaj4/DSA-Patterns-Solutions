"""
Qn. Remove All Adjacent Duplicates In String II

We are given a string s and an integer k.

Whenever k consecutive identical characters appear,
remove them from the string.

Keep removing such groups until no more removals are possible.

Return the final string.
"""

"""
Solution :

Maintain a stack storing:

    [character, frequency]

For every character in the string:

1. If stack is empty OR current character is different from stack top:
      push [character, 1]

2. If current character is same as stack top:
      check if frequency is already k - 1

      If yes:
          current character completes a group of k
          remove the entire group by popping the stack
          skip current character

      Else:
          increase frequency by 1

After processing the entire string:

Rebuild the answer by repeating every character
according to its stored frequency.

Return the final string.
"""

"""
Example :

s = "deeedbbcccbdaa"
k = 3

d  -> [(d,1)]

e  -> [(d,1),(e,1)]

e  -> [(d,1),(e,2)]

e  -> frequency already k-1 (=2)
      current e completes group of 3

      pop e

      [(d,1)]

d  -> [(d,2)]

b  -> [(d,2),(b,1)]

b  -> [(d,2),(b,2)]

c  -> [(d,2),(b,2),(c,1)]

c  -> [(d,2),(b,2),(c,2)]

c  -> frequency already k-1 (=2)
      current c completes group of 3

      pop c

      [(d,2),(b,2)]

d  -> frequency already k-1 (=2)
      current d completes group of 3

      pop d

      [(b,2)]

a  -> [(b,2),(a,1)]

a  -> [(b,2),(a,2)]

Final Answer = "aa"
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1][0] == ch:

                if stack[-1][1] == k - 1:
                    stack.pop()
                    continue

                stack[-1][1] += 1

            else:
                stack.append([ch, 1])

        res = ""

        for ch, freq in stack:
            res += ch * freq

        return res
        # res = []
        # for ch,freq in stack:
        #     res.append(ch * freq)
        
        # return "".join(res)