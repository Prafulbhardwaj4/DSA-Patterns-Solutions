"""
Qn. Given an array, we need to find number of triplets, whose sum is less than target
"""

"""
Solution :

We will sort the array, and find sum of first triplet(1st, 2nd, and last element),
if sum + or = target we will shift the right pointer 
and if sum is less than sum, then we will increase count till r-l
and at last return count
"""

def countTriplet(self, sum, arr):
    arr.sort()
    n = len(arr)
    count = 0

    for i in range(n-2):
        l = i + 1
        r = n - 1

        while l < r:
            cur_sum = arr[i] + arr[l] + arr[r]

            if cur_sum >= sum:
                r -= 1
            else:
                count += (r-l)
                l += 1
    return count