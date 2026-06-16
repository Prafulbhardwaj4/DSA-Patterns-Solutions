"""
Qn. We are given an array, we need to find the maximum contiguous array with equal number of
    0s and 1s

"""

"""
Solution :

Here -> X(number of Zeros) and Y(Number of Ones)
And, we are finding X - Y = 0


"""

"""
Example Array -> [0,1,1,1,1,1,0,0,0]

"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        f = {}
        one = zero = 0
        res = 0

        for n in range(len(nums)):
            if nums[n] == 0:
                zero += 1
            else:
                one += 1
            
            diff = zero - one

            if diff == 0:
                res = max(res,n+1)
            
            if diff not in f:
                f[diff] = n
            
            le = n - f[diff]
            res = max(res,le)
        return res