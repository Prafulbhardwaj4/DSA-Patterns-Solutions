"""
Qn.

Given a string,

Need to find the length of the longest substring
having all unique characters.

No character should repeat inside the substring.

"""

"""
Solution :

We need the longest substring with no repeating characters.

Since we are dealing with a substring,
Sliding Window can be used.

We maintain a window from l to h.

hashMap stores frequency of characters
present inside current window.

Observation :

If all characters are unique,

Window Length = Number of Distinct Characters

(h - l + 1) = len(hashMap)

If a duplicate character exists,

Window Length > Number of Distinct Characters

(h - l + 1) > len(hashMap)

So whenever :

len(hashMap) < (h - l + 1)

it means some character is repeating.

In that case we need to shrink the window
from the left.

Decrease frequency of s[l].

If frequency becomes 0,
remove that character from hashMap.

Keep shrinking until :

len(hashMap) == (h - l + 1)

which means all characters inside current window
are unique again.

Once window becomes valid,

calculate its length :

h - l + 1

and update answer.

Continue expanding h.

At the end,

res stores the length of the longest substring
containing only unique characters.

"""


def lengthOfLongestSubstring(self, s: str) -> int:
    l = h = 0
    n = len(s)
    res = 0
    hashMap = {}
    k = h - l + 1

    while h < n:
        hashMap[s[h]] = hashMap.get(s[h],0) + 1
        
        while len(hashMap) < (h-l+1):
            hashMap[s[l]] -= 1
            if hashMap[s[l]] == 0:
                del hashMap[s[l]]
            l += 1
        
        le = h - l + 1
        res = max(res,le)
        h += 1
    return res