"""
Qn.

Given 2 strings :

s -> main string
t -> target string

Need to find the minimum length substring of s
which contains all characters of t
(including their frequencies).

If no such substring exists,
return empty string.

"""

"""
Solution 

This is a Variable Size Sliding Window problem.

We need the smallest window in s
that contains all characters of t.

First we store frequencies of t in need.

need[ch] tells how many times that character
must be present in the window.

window[ch] stores frequencies of characters
currently present inside the sliding window.

required = len(t)

This represents how many characters are still needed
to make the current window valid.

Example :

s = "ADOBECODEBANC"
t = "ABC"

Initially :

required = 3

As we expand the window,

whenever we add a character which is needed,

and its frequency inside window does not exceed
the required frequency,

we reduce required by 1.

Example :

Need :

A -> 1
B -> 1
C -> 1

Window gets :

A

required becomes 2

Window gets :

A,B

required becomes 1

Window gets :

A,B,C

required becomes 0

Now current window contains all required characters.

So we enter shrinking phase.

While required == 0 :

Current window is valid.

Calculate its length :

right - left + 1

If this length is smaller than previously found answer,

store :

min_len
start

Now try removing characters from left.

Before removing,

check whether that character is important.

If removing it causes frequency inside window
to become less than required frequency,

window becomes invalid.

So :

required += 1

and shrinking stops.

Then expansion starts again.

This follows the same pattern :

Keep hiring until all requirements are met.

Once requirements are met,

start firing until requirements break.

Then hire again.

At every valid window,

we try to minimize its length.

At the end :

If no valid window was found,
return "".

Otherwise return :

s[start : start + min_len]

which is the minimum window substring.

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = [0] * 256
        window = [0] * 256

        for ch in t:
            need[ord(ch)] += 1

        required = len(t)  # chars still needed

        left = 0
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            c = ord(s[right])

            window[c] += 1

            if need[c] > 0 and window[c] <= need[c]:
                required -= 1

            while required == 0:
                curr_len = right - left + 1

                if curr_len < min_len:
                    min_len = curr_len
                    start = left

                left_char = ord(s[left])

                if need[left_char] > 0 and window[left_char] <= need[left_char]:
                    required += 1

                window[left_char] -= 1
                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]