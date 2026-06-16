
"""
Qn. Given an array, we need to find a subarray with maximum subarray sum,
    given we can allowed to delete one element fron any subarray to maximize the sum

"""

"""
Explanation :

We have some marks : English(89), Hindi(87), Physics(30), Math(20), Chemistry(5), Drawing(86)

We iterate to each subject, 
English we will store, Hindi we will store, 
and then we reach to physics, we will see marks are too low, i cannot store that, so you ignore that

so you use your power on one deletion

but, when you iterate to math you encounter with a score of 20, but you cannot ignore it as you have already used your power

so to solve this type of question, you need to have 2 datas
one where you have not used your data yet
another one where you have already used your data

-> When you reach physics, 

And you chose not to use your power 
you'll have 2 options, one where you add the marks to sum till arr[i-1]
or you'll ignore the sum till arr[i-1], and just update the sum to arr[i]

And if you want to use your power
you'll have 2 options, one where power is already used, and you just add arr[i]
or you'll ignore the exact element arr[i], and use sum till arr[i-1]

"""

"""
Solution :

We are allowed to delete at most one element from any subarray
to get the maximum possible subarray sum.

So at every index, we track two possibilities:

1) noDelete
   -> Maximum subarray sum ending at current index
   -> when we have NOT deleted any element yet

2) oneDelete
   -> Maximum subarray sum ending at current index
   -> when we HAVE already deleted one element earlier

Idea :

We process the array one element at a time.

---------------------------------------
CASE 1: No deletion used yet
---------------------------------------

For noDelete, we follow normal Kadane logic:

Either:
- extend previous subarray
- or start fresh from current element

So:
noDelete = max(noDelete + arr[i], arr[i])

---------------------------------------
CASE 2: One deletion is used
---------------------------------------

For oneDelete, we have two choices:

1) We already used deletion earlier:
   -> extend previous subarray with current element
   -> oneDelete + arr[i]

2) We use deletion at current position:
   -> skip current element
   -> so we take prevNoDelete (best sum till i-1 without deletion)

So:
oneDelete = max(oneDelete + arr[i], prevNoDelete)

---------------------------------------
Key idea of prevNoDelete:
---------------------------------------

If we skip arr[i], we directly carry forward the best
subarray sum ending at i-1 without using deletion.

---------------------------------------
Final Answer:
---------------------------------------

At each step, the answer can come from either state:

res = max(res, noDelete, oneDelete)

We take the best among:
- normal Kadane (no deletion)
- Kadane with one deletion used

"""

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        noDelete = arr[0]
        oneDelete = 0
        res = arr[0]

        for i in range(1,len(arr)):
            prevNoDelete = noDelete
            noDelete = max(noDelete+arr[i],arr[i])
            oneDelete = max(oneDelete+arr[i],prevNoDelete)
            res = max(res,noDelete,oneDelete)
        return res

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        noDelete = arr[0]
        oneDelete = 0
        res = arr[0]

        for i in range(1,len(arr)):
            prevNoDelete = noDelete
            noDelete = max(noDelete+arr[i],arr[i])
            oneDelete = max(oneDelete+arr[i],prevNoDelete)
            res = max(res,noDelete,oneDelete)
        return res