"""
Qn. There are 2 sorted arrays we need to merge them and the new array should also be sorted
    On leetcode -> nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    And we do not need to return anything just update the nums1
"""

"""
Solution :

So firstly we will initiate 2 pointers one for each array, and a new empty array
Then a run a loop while pointer 1 is < len(nums1) and pointer 2 is < len(nums2)
If 1st element of first array is small we will append it and increase the pointer 1 value
else we will append we will append the 1st element of second element and increase the pointer 2 value
Then if r>n, we will keep on appending nums1 elements to merge array, while l<n  
And if l>n, we will keep on appending nums2 elements to merge array, while r<n
And at last we will update nums1[:] = merge  
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        l = 0
        r = 0
        merged = []

        while l < m and r < n:
            if nums1[l] <= nums2[r]:
                merged.append(nums1[l])
                l += 1
            else:
                merged.append(nums2[r])
                r += 1

        while l < m:
            merged.append(nums1[l])
            l += 1

        while r < n:
            merged.append(nums2[r])
            r += 1

        nums1[:] = merged