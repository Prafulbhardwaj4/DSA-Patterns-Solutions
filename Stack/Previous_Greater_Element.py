"""
Qn.

Given an array nums, find the Previous Greater Element for every element.

The Previous Greater Element of nums[i] is the first element on its left
that is strictly greater than nums[i].

If no such element exists, return -1 for that position.

Example:

Input  : [4, 1, 2, 5, 3]
Output : [-1, 4, 4, -1, 5]

Explanation:
For 4 -> no greater element on left => -1
For 1 -> 4 is the first greater element on left => 4
For 2 -> 4 is the first greater element on left => 4
For 5 -> no greater element on left => -1
For 3 -> 5 is the first greater element on left => 5

"""

"""
Solution :

We will use a Monotonic Decreasing Stack.

The stack will store elements from the left side of the array in decreasing order.

For every current element nums[i]:

1. Pop all elements from the stack which are less than or equal to nums[i]
   because they can never become the Previous Greater Element for the current
   element or any future larger element.

2. After popping:
   - If stack becomes empty, there is no greater element on the left,
     so result[i] = -1.
   - Otherwise, stack[-1] is the nearest greater element on the left,
     so result[i] = stack[-1].

3. Push nums[i] into the stack for future elements.

Each element is pushed once and popped at most once.

TC -> O(n)
SC -> O(n)

"""

def previous_greater(nums):
    stack = []
    res = [0] * len(nums)
    res[0] = -1
    stack.append(nums[0])

    for i in range(1, len(nums)):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]

        stack.append(nums[i])

    return res