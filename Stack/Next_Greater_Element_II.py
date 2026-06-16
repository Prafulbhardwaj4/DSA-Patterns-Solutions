"""
Qn. Next Greater Element II

We are given a circular array, and for each element we need to find the next greater element.
If it does not exist, return -1.

A circular array means after last element we go back to first element.
"""

"""
Solution :

We maintain a monotonic decreasing stack (stack will store elements).

We traverse the array from right to left, but since it is circular,
we simulate it by going 2 times around the array (2 * n traversal).

At each element:

We remove all elements from stack which are smaller or equal than current element
because they cannot be next greater for current or previous elements.
After popping:
if stack is not empty → top of stack is next greater element
else → no greater element exists (-1)
Then we push current element into stack

We only fill result array during the first pass (i < n),
second pass is only for simulation of circular behavior.
"""

"""
Example :

nums = [1, 2, 1]

step idea:

1 → next greater = 2
2 → no greater = -1
last 1 → circular sees 2 → 2

Answer = [2, -1, 2]
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        res = [-1] * len(nums)

        for i in range(len(nums)-2,-1,-1):
            stack.append(nums[i])

        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1]

            stack.append(nums[i])
        return res