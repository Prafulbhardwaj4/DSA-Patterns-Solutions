"""
Qn.

Given an array nums, find the Previous Smaller Element for every element.

The Previous Smaller Element of nums[i] is the first element on its left
that is strictly smaller than nums[i].

If no such element exists, return -1 for that position.

Example:

Input  : [4, 1, 2, 5, 3]
Output : [-1, -1, 1, 2, 2]

Explanation:
For 4 -> no smaller element on left => -1
For 1 -> no smaller element on left => -1
For 2 -> 1 is the first smaller element on left => 1
For 5 -> 2 is the first smaller element on left => 2
For 3 -> 2 is the first smaller element on left => 2

"""

"""
Solution :

We will use a Monotonic Increasing Stack.

The stack will store elements from the left side of the array in increasing order.

For every current element nums[i]:

1. Pop all elements from the stack which are greater than or equal to nums[i]
   because they cannot be the Previous Smaller Element for the current element.

2. After popping:
   - If the stack becomes empty, there is no smaller element on the left,
     so result[i] = -1.
   - Otherwise, stack[-1] is the nearest smaller element on the left,
     so result[i] = stack[-1].

3. Push nums[i] into the stack so that it can be used for future elements.

Each element is pushed into the stack once and popped at most once.

TC -> O(n)
SC -> O(n)

"""

def previous_smaller(nums):
    if not nums:
        return []

    stack = []
    res = [0] * len(nums)

    res[0] = -1
    stack.append(nums[0])

    for i in range(1, len(nums)):
        while stack and stack[-1] >= nums[i]:
            stack.pop()

        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]

        stack.append(nums[i])

    return res