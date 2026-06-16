
"""
Qn. We are given an array, with both positive and negative values,
    need to find a subarrya with minimum sum

"""

"""
Solution :

start with best ending = a[0]
As of now we have no data, so initiate ans = a[0]

Then run a loop from i to n-1
then update best, by taking minimum of, a[i] and best+a[i]
then update ans, by taking minimum of, ans and best

at last return ans

"""


class Solution:
    def smallestSumSubarray(self, A, N):
        best = A[0]
        ans = A[0]
        
        for n in range(1,N):
            best = min(best+A[n],A[n])
            ans = min(ans,best)
        return ans