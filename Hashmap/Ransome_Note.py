"""
Qn. We are given 2 strings, 
    One is Ransome, and
    One is magazine

    We need to find if we can create Ransome string using characters of magazine or not

"""

"""
Example :

Ransome -> "aab"
Magazine -> "aabbcb"

Ransome -> "aa"
Magazine -> "aab"

"""
"""
Solution :

We will first store frequencies of both strings
in need -> ransomnote, means how many minimum are needed
in have -> how many, magazine have

then (taking example as -> "aab" and :aabbcb")
for ch in need, ch at first iteration will be = 'a'
                ch at second iteration will be = 'b'

for each iteration we will check, that if, "have" has less character frequency then need[ch],
we will return False

and if program comes out of the loop, means if condition never gets satisfied, 
we will return True

"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = {} 
        have = {}

        for i in ransomNote:
            need[i] = need.get(i,0) + 1

        for i in magazine:
            have[i] = need.get(i,0) + 1
        
        for ch in need:
            if have.get(ch,0) < need[ch]:
                return False
        return True