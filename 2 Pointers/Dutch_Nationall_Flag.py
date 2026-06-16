"""
Qn. We are given an array(with only 0, 1, and 2), we need to rearrange it in such a way([0,1,2]).
    we cannot sort the array (Leetcode qn - 75)
"""

"""
Solution :

1) Brute Force -> Create 3 different arrays and then join them in needed sequence
   or count the number of 0s, 1s, and 2s.

   TC -> O(n)
   SC -> O(n)

2) Optimised -> Create 3 variables, traverse through the main array,
   count the occurrences of 0, 1, and 2 and overwrite the array.

   TC -> O(n)
   SC -> O(1)

   But it's a 2-pass approach because we traverse the array twice.

3) Dutch National Flag Algorithm (3 Pointers) -> 1-pass approach

   low  -> Boundary for 0s
   mid  -> Current element being processed
   high -> Boundary for 2s

   Rules:
   - If arr[mid] == 0:
       Swap arr[low] and arr[mid]
       low += 1
       mid += 1

   - If arr[mid] == 1:
       mid += 1

   - If arr[mid] == 2:
       Swap arr[mid] and arr[high]
       high -= 1
       (Don't increment mid because the swapped element
        needs to be checked)

   TC -> O(n)
   SC -> O(1)
"""

def arrSort(self,nums):
    l = 0
    m = 0
    h = len(nums) - 1

    while m <= h:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m],nums[l]
            l += 1
            m += 1
        elif nums[m] == 1:
            m += 1
        else:
            nums[m],nums[h] = nums[h], nums[m]
            h -= 1
    return nums