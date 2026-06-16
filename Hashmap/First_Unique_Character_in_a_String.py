"""
Qn. We are given a string, and we need to find the first unique character of that string. And if no 
    such element occurs, return -1

"""
"""
Example :

"abcab"

in this one, we will first go to s[0] we will check if it's unique or not,
if yes then return, otherwise s[1],s[2]...and goes on

And to check whether an element is unique or not, we will use hashmap
{
a-> 2
b-> 2
c-> 1
}

Answer will be c
"""
"""
Solution :

We will first calculate the frequency of each character of string,
and store in hashmap, where key -> character, and value -> frequency

then we will check if f[s[i]] == 1, we will return i(that character)
f[s[i]] -> means string character's frequency stored in hashmap

and if no such character, return -1

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = {}

        for i in s:
            f[i] = f.get(i,0) + 1
        
        for i in range(len(s)):
            if f[s[i]] == 1:
                return i
            
        return -1