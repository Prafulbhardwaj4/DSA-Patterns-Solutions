"""
Qn. Given an array of integers, and a number k. We need to return the maximum sum of a subarray of 
    size k

"""

"""
Solution :

Since size of subarray is fixed,

we can use Fixed Size Sliding Window.

Window size = k

First we calculate the sum of the first window.

Example :

arr = [2,5,1,8,2]
k = 3

First Window :

[2,5,1]

cur_sum = 8

Initially :

res = cur_sum

Now instead of calculating every window sum from scratch,

we slide the window by one position.

To move window :

1) Remove left element from current sum

   cur_sum -= arr[l]

2) Move both pointers

   l += 1
   h += 1

3) Add new right element

   cur_sum += arr[h]

This gives the sum of the next window in O(1) time.

Example :

Previous Window :

[2,5,1]

Sum = 8

Next Window :

[5,1,8]

Remove 2
Add 8

New Sum = 14

After every window,

compare current sum with answer and update maximum.

res = max(res, cur_sum)

Continue until last possible window is processed.

At the end,

res stores the maximum sum among all subarrays
having size exactly k.

"""


def sumArray(self, arr, k):
    n = len(arr)

    l = 0
    h = k-1
    res = 0
    cur_sum = 0
    
    for i in range(l,h+1):
        cur_sum += arr[i]

    res = cur_sum

    while h<n-1:
        cur_sum -= arr[l]
        
        l += 1
        h+= 1
            
        cur_sum += arr[h]

        res = max(res,cur_sum)

    
    return res