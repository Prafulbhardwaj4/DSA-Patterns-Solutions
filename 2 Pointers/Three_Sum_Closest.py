"""
Qn. Find the sum of a triplet which is closest to the given target.

"""

"""
Pattern :

It is 2 Sum only, but we need to use 2 Sum for each i.

Brute     ->   Use 3 loops.
               First loop(i) from 0 to n-3,
               Second loop(j) from i+1 to n-2,
               Third loop(k) from j+1 to n-1.
               Find sum = a[i] + a[j] + a[k]
               Keep updating the answer whose difference
               from target is minimum.
               TC -> O(n^3)

Optimised ->   Fix a[i].
               Now we need:
               a[i] + x + y ≈ target
               Therefore:
               x + y ≈ target - a[i]
               Since the array is sorted, we can use the
               2-pointer approach to move towards the target.
"""

"""
Solution :

Firstly sort the array.
Store the sum of the first 3 elements as the initial answer
(closest_sum).
Run a loop from 0 to n-3.
For every i :
l = i + 1
r = n - 1

Now calculate :
curr_sum = a[i] + a[l] + a[r]
If the difference of curr_sum from target is smaller than
the difference of closest_sum from target,
update closest_sum.
If curr_sum == target,
return target immediately because we cannot get any closer.
If curr_sum < target,
increase l by 1 to make the sum larger.
If curr_sum > target,
decrease r by 1 to make the sum smaller.
Continue until l >= r.
Finally return closest_sum.

TC -> O(n^2)
SC -> O(1)

"""


def threeSumClosest(self,nums,target):
    nums.sort()
    n = len(nums)

    closest_sum = nums[0] + nums[1] + nums[2]    

    for i in range(n-2):

        l = i + 1
        r = n - 1

        while l < r:

            cur_sum = nums[i] + nums[l] + nums[r]

            if abs(cur_sum - target) < abs(closest_sum - target):
                closest_sum = cur_sum

            if cur_sum == target:
                return target
            
            elif cur_sum < target:
                l += 1
            
            else:
                r -= 1
    return closest_sum