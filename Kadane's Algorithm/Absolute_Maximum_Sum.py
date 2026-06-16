"""
Qn. We are given an array, with both positive and negative values,
    need to find absolute maximum sum

"""

"""
Example :

nums = [1,-3,2,3,-4]

Possible subarray sums :

[1]      -> 1
[-3]     -> -3
[2,3]    -> 5
[-3,2,3] -> 2
[1,-3]   -> -2

Maximum positive sum = 5
Minimum (most negative) sum = -3

Absolute maximum sum = max(abs(5),abs(-3))
                     = 5

"""

"""
Solution :

We need the maximum absolute subarray sum.

Absolute value can become maximum in 2 ways :

1. We get a very large positive subarray sum
2. We get a very large negative subarray sum

So we will track both :

maxEnd -> maximum subarray sum ending at current index
minEnd -> minimum subarray sum ending at current index

Initially both are set to nums[0].

For every element, we have 2 choices :

For maxEnd :
Either extend previous subarray
or start a new subarray from current element

maxEnd = max(maxEnd + nums[i], nums[i])

For minEnd :
Either extend previous minimum subarray
or start a new subarray from current element

minEnd = min(minEnd + nums[i], nums[i])

At every iteration :

maxEnd gives best positive sum ending here
minEnd gives most negative sum ending here

We compare current answer with :
maxEnd
abs(minEnd)

because absolute maximum can come from either side.

If loop finishes,
ans will contain the maximum absolute subarray sum.

"""

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxEnd = minEnd = nums[0]
        ans = abs(nums[0])

        for i in range(1,len(nums)):
            maxEnd = max(maxEnd+nums[i],nums[i])
            minEnd = min(minEnd+nums[i],nums[i])
            ans = max(ans,maxEnd,abs(minEnd))
        return ans