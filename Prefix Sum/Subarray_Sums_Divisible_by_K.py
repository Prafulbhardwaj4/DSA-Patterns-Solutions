"""
Qn. We are given an array, we need to find count of subarrays
    whose sum is divisible by k

"""

"""
Solution :

We will use the Prefix Sum + HashMap approach.

The idea is that if two prefix sums have the same remainder
when divided by k, then the subarray between them has a sum
that is divisible by k.

Suppose:
    prefixSum[j] % k == prefixSum[i] % k

Then:
    (prefixSum[j] - prefixSum[i]) % k == 0

which means the sum of the subarray between i+1 and j
is divisible by k.

We will maintain:
- cur_sum : Running prefix sum till current index.
- f : Stores frequency of each remainder encountered.
- res : Stores the total count of valid subarrays.

Initially, we store f[0] = 1.
This handles the case where the prefix sum itself
is divisible by k.

For every element in the array:
- Update cur_sum.
- Compute remainder = cur_sum % k.
- If this remainder has appeared before,
  then all previous occurrences form valid subarrays
  ending at the current index.
- Add the frequency of this remainder to the answer.
- Update the frequency of the current remainder.

At the end, return res which contains the total number
of subarrays whose sum is divisible by k.

Time Complexity : O(n)
Space Complexity : O(n)
"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        f = {}
        f[0] = 1
        cur_sum = 0
        res = 0

        for i in nums:
            cur_sum += i
            rem = cur_sum % k
            if rem < 0:
                rem += k
            freq = f.get(rem,0)
            res += freq
            f[rem] = f.get(rem,0) + 1
        return res