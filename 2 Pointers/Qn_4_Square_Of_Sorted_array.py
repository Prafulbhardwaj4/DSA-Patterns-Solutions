"""
Qn. Given a sorted array (negative values can also be present),
    we need to return a new sorted array containing the squares of all elements.

"""

"""
Example:
nums = [-4,-1,0,3,10]

After squaring:
[16,1,0,9,100]

But this is not sorted.
Required output:
[0,1,9,16,100]

"""

"""
Solution :

Since the original array is already sorted, all negative numbers will appear
on the left side and all non-negative numbers will appear on the right side.

We will first separate the array into 2 arrays:
1. neg -> stores all negative numbers
2. pos -> stores all non-negative numbers

Now there can be 3 cases:

Case 1:
If neg is empty,
then the entire array already contains only non-negative numbers.
After squaring, the order remains sorted.
So directly return squares of all elements in pos.

Case 2:
If pos is empty,
then the entire array contains only negative numbers.
After squaring, the order becomes decreasing.
Example:
[-5,-3,-1] -> [25,9,1]

So we square all elements and reverse the result
to make it sorted in increasing order.

Case 3:
Both neg and pos exist.

First square all elements in neg and reverse it.

Reason:
neg is sorted in increasing order:
[-7,-4,-2]

After squaring:
[49,16,4]

This becomes decreasing.

After reversing:
[4,16,49]

Now neg squares are sorted.

Similarly square all elements in pos.
Since pos already contains non-negative values in sorted order,
its squares will also remain sorted.

At this point we have 2 sorted arrays:
1. squared neg array
2. squared pos array

Now the problem reduces to:
"Merge two sorted arrays."

Use two pointers:
l -> points to neg array
r -> points to pos array

Compare elements from both arrays and insert the smaller one
into a third array called merged.

Once one array gets exhausted,
append all remaining elements from the other array.

Finally return merged.

TC -> O(n)
SC -> O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        neg = []
        pos = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        if len(neg) == 0:
            return [x*x for x in pos]
        
        if len(pos) == 0:
            res = [x*x for x in neg]
        
        neg = [x*x for x in neg][::-1]
        pos = [x*x for x in pos]
        m,n = len(neg), len(pos)
        merged = []

        l = r = 0
        while l < m and r < n:
            if neg[l] <= pos[r]:
                merged.append(neg[l])
                l += 1
            else:
                merged.append(pos[r])
                r += 1

        while l < m:
            merged.append(neg[l])
            l += 1

        while r < n:
            merged.append(pos[r])
            r += 1

        return merged