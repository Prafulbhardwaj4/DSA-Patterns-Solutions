"""
Qn. We are given a string, we need to find the longest palindrome that can be created using the 
    characters of that string 

"""

"""
Example : "abccccdd"
Output -> 7

Explanation -> "dccaccd"

in this string, we have 
a -> 1
b -> 1
c -> 4
d -> 2

What we can do, buy using even number of characters, or using pairs of 2 we can make palindrome
for example -> cc, cccc, dccccd

longest till now is adding freuency of even characters -> 4 + 2 = 6

now at center we can add any characters of odd frequency

in this we can add, either a or b, the longest will be 7 only
"""

"""
Solution :

We will first initiate 
res with 0
odd_Found with False

then run a loop to store frequencies of character's of string om string

then second loop on hashmap
if freq of ch is even, 
just increase res by 1

if odd,
increase res by frequency of character - 1
and also switch odd_found to True

after loop,
if odd_found is True, just increase res by 1

and at last,
return res

"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        f = {}
        res = 0
        odd_Found = False

        for ch in s:
            f[ch] = f.get(ch,0) + 1
        
        for ch in f:
            if f[ch] % 2 == 0:
                res += f[ch]
            else:
                res += f[ch] - 1
                odd_Found = True
        
        if odd_Found:
            res += 1

        return res