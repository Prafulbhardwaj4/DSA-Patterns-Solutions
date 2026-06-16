"""
Qn. We are given an array, with both positive and negative values,
    need to find maximum subarray sum in a circular array

    Circular means after last index,
    array can continue again from first index

"""

"""
Example :

nums = [1,-2,3,-2]

Normal maximum subarray :
[3] -> sum = 3

Circular maximum subarray :
No better answer exists

Answer = 3


nums = [5,-3,5]

Normal maximum subarray :
[5,-3,5] -> 7

Circular maximum subarray :
Take last 5 and first 5

sum = 10

Answer = 10

"""

"""
Solution :

There are 2 possible cases :

Case 1 :
Maximum subarray lies completely inside array
(without using circular property)

For this we use Kadane's Algorithm.

maxEnd -> maximum subarray sum ending at current index
maxSum -> overall maximum subarray sum


Case 2 :
Maximum subarray uses circular property

Instead of finding circular subarray directly,
we find minimum sum subarray.

Why ?

If we remove the minimum sum subarray from total array,
remaining elements will form the maximum circular subarray.

Example :

nums = [5,-3,5]

Total Sum = 7

Minimum subarray = [-3]

Remaining circular part = [5,5]

Circular sum = Total Sum - Minimum Sum
             = 7 - (-3)
             = 10

So we also track :

minEnd -> minimum subarray sum ending at current index
minSum -> overall minimum subarray sum

After loop :

maxSum = best normal subarray sum
tSum - minSum = best circular subarray sum

Answer will be maximum of both.

Special Case :

If all numbers are negative,

then minSum becomes equal to total sum.

tSum - minSum becomes 0,
which is not a valid answer because we cannot take
an empty subarray.

So if maxSum < 0,
we directly return maxSum.

Otherwise return :

max(maxSum, tSum - minSum)

"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxEnd = minEnd = nums[0]
        maxSum = minSum = nums[0]
        tSum = sum(nums)

        for i in range(1,len(nums)):
            maxEnd = max(maxEnd+nums[i],nums[i])
            maxSum = max(maxSum,maxEnd)

            minEnd = min(minEnd+nums[i],nums[i])
            minSum = min(minSum,minEnd)

        if maxSum < 0:
            return maxSum

        return max(maxSum,tSum-minSum)