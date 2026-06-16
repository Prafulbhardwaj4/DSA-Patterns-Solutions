"""
Qn. We are given a case study, where there is a garden with 3 types of trees we need to fill 2 
    baskets with distinct fruits and calculate maximum number of fruits we can have

"""

"""
Solution :

We will first create a hashMap, for frequencies of fruits
then we will run a loop from 0 to last element of array
then inside the loop we will update the frequency of each fruit
then there'll be 3 cases, where len(hashMap) == k, <k, >k

for >k -> we will first decrease the frequency of fruits[l] from hashMap
and if frequency of fruits[l] becomes 0 we will delete it from hashMap to reduce length
and increase l

we are asked for atmost 2 types of fruits 
so for =k, <k -> we will calculate len(hashMap) by h - l + 1, 
then we will find maximum of res and length
and increase h

And return result

TC -> O(n)
SC -> O(1)

"""

def fruitsIntoBasket(self,fruits):
    n = len(fruits)
    k = 2
    l = h = 0
    res = -1
    hashMap = {}

    while h < n:
        hashMap[fruits[h]] = hashMap.get(fruits[h],0) + 1

        while len(hashMap) > k:
            hashMap[fruits[l]] -= 1
            if len(hashMap[fruits[l]]) == 0:
                del hashMap[fruits[l]]
            l += 1

        le = h - l + 1
        res = max(le,res)
        
        h += 1

    return res 