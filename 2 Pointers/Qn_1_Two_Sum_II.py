"""
Qn. Given an sorted array(if not sorted we will sort it) [2,7,11,15]
    We need to find 2 numbers whose sum will be = Target(9)

"""

"""
Solution :

We will sort the array first(if not sorted)
If in this one we check 2+15 that will be = 17, which is greater than the target
then in next iteration we know the array is sorted by now, so we will not check 7+15,
as it will anyhow be greater than the target, 
so in that case, we need to update the left pointer,
and vice versa, till we get our target

If the sum is not available, so the pointer will stop when both the pointers will be at same index
So we will run while loop till i<j

TC -> O(n logn) hash map apprach given O(n), in  this one[sorting = O(n logn) and iteration - O(n), and bigger is O(n)]
SC -> O(1), but hashmap takes O(n) SC


"""

from typing import List
def twoSum(self,numbers: List[int], target: int) -> List[int]:
    l = 0
    r=len(numbers)-1
    
    while l<r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l+1,r+1]
        elif sum < target:
            l += 1
        elif sum > target:
            r -= 1
    return