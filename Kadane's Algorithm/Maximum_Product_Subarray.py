
"""
Qn. We are given an array, with both positive and negative values,
    need to find a subarrya with maximum product

"""

"""
Solution :

start maxEnd and mixEnd with a[0]
As of now we have no data, so initiate ans = a[0]

Then run a loop from i to n-1
then take 3 variables
v1 = nums[n]
v2 = maxEnd * nums[n]
v3 = minEnd * nums[n]

then calculate :
maxEnd = max of all 3
minEnd = min of all 3

ans = max of ans and maxEnd(we can also find max(maxEnd,minEnd), but that will be maxEnd only)
at last return ans
    
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxEnd = minEnd = ans = nums[0]

        for n in range(1,len(nums)):
            v1 = nums[n]
            v2 = maxEnd * nums[n]
            v3 = minEnd * nums[n]

            maxEnd = max(v1,max(v2,v3))
            minEnd = min(v1,min(v2,v3))

            ans = max(ans,maxEnd)
        return ans