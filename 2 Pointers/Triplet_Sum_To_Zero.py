"""
Qn. Find triplets whose some is equal to 0, and the answer should be unique as well

"""

"""
Pattern :

It is 2 sum qn only, but we need to use two sum for each i 

Brute     ->   3 loops with first one(i) from 0, 2nd(j) from i+1, 3rd(k) from  j+1
               TC -> O(n^3)

Optimised ->   In Brute we were finding a[i]+ x + y = 0
               Now we will find x + y = -a[i]
               That is two sum

"""

"""
Solution :

Firstly we will sort the array
then run a loop on array from 0 to n-2,
and if i>0 and a[i] == a[i-1] then we continue,
Otherwise,
l = i+1
r = n-1(where n = len(arr))
sum = -1 X a[i]
then we will do same as 2 sum, initiate 2 pointers,
one(l) from 0, 2nd(r) from  len(arr)-1
But now if summ == target, firstly store those valuse in array,
then shift both pointers by 1 
while, l<n and a[l] is equal to previous element we will increase l
and if r>=0 and a[r] is equal to next element we will decrease r
if sum smaller than target increase l, if sum greater than decrease r
then at last return arr[arr]

"""
def threeSum(self,nums):
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i+1
        r = n-1

        target = -nums[i]

        while l < r:
            cur_sum = nums[l]+nums[r]

            if cur_sum == target:
                res.append([nums[i],nums[l],nums[r]])

                l += 1
                r -= 1

                while l<r and nums[l] == nums[l-1]:
                    l += 1
                while l<r and nums[r] == nums[r+1]:
                    r -= 1
            
            elif cur_sum < target:
                l += 1
            else:
                r -= 1
    return res