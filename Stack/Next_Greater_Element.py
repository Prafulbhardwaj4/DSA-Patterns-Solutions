"""
Qn.

Given an array nums, find the Next Greater Element for every element.

The Next Greater Element of nums[i] is the first element on its right
that is strictly greater than nums[i].

If no such element exists, return -1 for that position.

Example:

Input  : [4, 1, 2, 5, 3]
Output : [5, 2, 5, -1, -1]

Explanation:
For 4 -> next greater is 5
For 1 -> next greater is 2
For 2 -> next greater is 5
For 5 -> no greater element on right => -1
For 3 -> no greater element on right => -1

"""

"""
Solution :

We use a Monotonic Decreasing Stack and traverse from right to left.

Idea:
We maintain a stack that stores possible candidates for next greater element.

For each element nums[i]:

1. Pop all elements from stack which are <= nums[i]
   because they cannot be the next greater element.

2. If stack becomes empty:
   - res[i] = -1
   Else:
   - res[i] = stack[-1]

3. Push nums[i] into the stack.

Each element is pushed and popped at most once, so time complexity is O(n).

TC -> O(n)
SC -> O(n)

"""

def next_greater(nums):
    if not nums:
        return []

    stack = []
    res = [0] * len(nums)

    res[len(nums) - 1] = -1
    stack.append(nums[len(nums) - 1])

    for i in range(len(nums) - 2, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]

        stack.append(nums[i])

    return res