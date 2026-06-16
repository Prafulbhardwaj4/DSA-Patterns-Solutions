"""
Qn. We are given an array, and we need to find the min. subarray whose elements sum is either equal 
    to or, greater than the target

"""

"""
Pattern : 

Company hiring and firing example

It will keep on hiring untill target meets, and the moment target meets, it will start firing untill the target is met, and the moment target doesn't meet it will again start hiring.

And the same loop continues till we reach the end of the array
"""


"""
Solution :

This is a Variable Size Sliding Window problem.

We need the minimum length subarray whose sum is
greater than or equal to target.

Using the hiring and firing analogy :

Hiring  -> Expand the window
         -> h moves right
         -> Add new employee (element)

Firing  -> Shrink the window
         -> l moves right
         -> Remove employee (element)

Initially :

l = 0
h = 0
cur_sum = 0

As h moves forward,

we keep adding nums[h] into cur_sum.

This is the hiring phase.

As long as cur_sum is smaller than target,

we keep hiring because target is not yet achieved.

The moment :

cur_sum >= target

current window becomes a valid answer.

Now our goal is not to increase the sum further.

We need the minimum length window.

So we start firing employees from the left.

Current window length :

h - l + 1

Update answer with minimum length found so far.

res = min(res, h - l + 1)

Then remove nums[l] from cur_sum
and move l forward.

We continue firing as long as :

cur_sum >= target

because a smaller valid window may still exist.

The moment :

cur_sum < target

window becomes invalid again.

So firing stops and hiring starts again.

This process continues until h reaches the end
of the array.

At the end :

If res was never updated,
it means no valid subarray exists.

Return 0.

Otherwise return res,
which stores the minimum length subarray
whose sum is greater than or equal to target.


TC -> O(n)
SC -> O(1)

"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = 0
        cur_sum = 0
        res =  float('inf')

        while h < n:
            cur_sum += nums[h]

            while cur_sum >= target:
                le = h - l + 1
                res = min(res, le)
                cur_sum -= nums[l]
                l += 1
            
            h += 1

        return 0 if res == float('inf') else res