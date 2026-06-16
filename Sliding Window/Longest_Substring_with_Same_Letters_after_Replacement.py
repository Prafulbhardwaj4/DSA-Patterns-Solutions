"""
Qn. Given a string consisting of uppercase characters,
    and an integer k,

    We can replace at most k characters.

    Need to find the length of the longest substring
    that can be converted into a string having all
    same characters after performing at most k replacements.

"""

"""
Solution :

We need the longest substring in which all characters
can become same using at most k replacements.

Observation :

For any window,

the character having maximum frequency should be kept as it is.

All remaining characters can be replaced.

Example :

Window = "AABAB"

Frequency :

A -> 3
B -> 2

maxf = 3

If we keep all A's unchanged,
we only need to replace B's.

Replacements needed :

Window Length - maxf
= 5 - 3
= 2

General Formula :

Replacements Needed =
(Current Window Length) - (Maximum Frequency Character)

If this value is <= k,
window is valid.

Otherwise window is invalid.

So we use Sliding Window.

hashMap stores frequencies of characters
inside current window.

maxf stores maximum frequency of any character
seen in current window.

For every iteration :

Add s[h] into hashMap.

Update maxf.

Now check validity :

(Current Window Length) - maxf

If this becomes greater than k,

it means more than k replacements are required.

So we shrink the window from left
until it becomes valid again.

For every valid window,

update answer with its length.

At the end,

res stores the length of the longest substring
that can be converted into all same characters
using at most k replacements.

"""

def LSWSLAR(self,s,k):
    n = len(s)
    l = h = 0
    res = 0
    maxf = 0
    hashMap = {}

    while h < n:
        hashMap[s[h]] = hashMap.get(s[h], 0 ) + 1
        maxf = max(maxf, hashMap[s[h]])

        while (h - l + 1) - maxf > k:
            hashMap[s[l]] -= 1
            l += 1
        
        res = max((h - l + 1), res)
        h += 1
    return res