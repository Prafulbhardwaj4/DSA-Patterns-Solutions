"""
Qn. We are given an array, we need to find total number of subarrays
    whose sum equals to k

"""

"""
Solution :

We will use the Prefix Sum + HashMap approach.

The idea is that if the current prefix sum is cur_sum,
then any previous prefix sum equal to (cur_sum - k)
indicates a subarray whose sum is exactly k.

Why?

Suppose:
    cur_sum = prefixSum[j]

We need:
    prefixSum[j] - prefixSum[i] = k

Rearranging:

    prefixSum[i] = cur_sum - k

So if we have previously seen a prefix sum equal to
(cur_sum - k), then the subarray between those positions
has sum exactly k.

We will maintain:
- cur_sum : Running prefix sum till current index.
- hashMap : Stores frequency of each prefix sum encountered.
- res : Stores the total count of valid subarrays.

Initially, we store hashMap[0] = 1.
This handles the edge case where a subarray starting
from index 0 itself has sum equal to k.

For every element in the array:
- Update cur_sum by adding the current element.
- Calculate required prefix sum = cur_sum - k.
- If this required prefix sum exists in hashMap,
  add its frequency to the answer because each occurrence
  represents a valid subarray ending at the current index.
- Store/update the frequency of the current prefix sum.

At the end, return res which contains the total number
of subarrays whose sum equals k.

Time Complexity : O(n)
Space Complexity : O(n)
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        hashMap = {}
        res = 0
        hashMap[0] = 1

        for i in nums:
            cur_sum += i
            ques = cur_sum - k
            freq = hashMap.get(ques,0)
            res += freq
            hashMap[cur_sum] = hashMap.get(cur_sum,0) + 1
        return res