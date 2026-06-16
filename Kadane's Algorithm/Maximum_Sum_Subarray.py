
"""
Qn. We are given an array, with both positive and negative values,
    need to find a subarrya with maximum sum

"""

"""
Solution :

start with best ending = a[0]
As of now we have no data, so initiate ans = a[0]

Then run a loop from i to n-1
then update best, by taking maximum of, a[i] and best+a[i]
then update ans, by taking maximum of, ans and best

at last return ans

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            best = max(best+nums[i],nums[i])
            ans = max(ans,best)
        
        return ans