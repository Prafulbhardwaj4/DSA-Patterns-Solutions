"""
Qn. Given a string(all lowercase characters), we need to find longest substring with k distinct 
    characters in it
"""

"""
Solution : 

We need to find the longest substring which contains exactly k distinct characters.

Since we are dealing with a substring,
we can use Sliding Window.

We maintain a window from l to h.

hashMap will store frequency of characters present inside current window.

Initially :

l = 0
h = 0

As h moves forward,

we add s[h] into hashMap.

Now there can be 3 cases :

Case 1 :
len(hashMap) < k

This means current window has less than k distinct characters.

We cannot calculate answer yet,
so keep expanding window.

Case 2 :
len(hashMap) == k

This means current window has exactly k distinct characters.

Current window length :

h - l + 1

Update answer with maximum length found so far.

Case 3 :
len(hashMap) > k

This means window has more than k distinct characters.

We need to shrink the window from left.

Decrease frequency of s[l].

If frequency becomes 0,
remove that character from hashMap.

Keep shrinking until distinct characters become <= k.

After handling all cases,
move h forward.

At the end,

res stores the length of longest substring
having exactly k distinct characters.

If no such substring exists,
res remains -1.

"""

def LSWKD(self,s,k):
    n = len(s)
    l = h = 0
    res = -1
    hashMap = {}
    
    while h < n:
        hashMap[s[h]] = hashMap.get(s[h],0) + 1
        
        while len(hashMap) > k:
            hashMap[s[l]] -= 1
            if hashMap[s[l]] == 0:
                del hashMap[s[l]]
            l += 1
        
        if len(hashMap) == k:
            le = h - l + 1
            res = max(le,res)
        
        h += 1
    return res