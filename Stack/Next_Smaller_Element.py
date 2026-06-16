"""
Qn.

Given an array nums, find the Next Smaller Element for every element.

The Next Smaller Element of nums[i] is the first element on its right
that is strictly smaller than nums[i].

If no such element exists, return -1 for that position.

Example:

Input  : [4, 1, 2, 5, 3]
Output : [1, -1, -1, 3, -1]

Explanation:
For 4 -> next smaller is 1
For 1 -> no smaller element on right => -1
For 2 -> no smaller element on right => -1
For 5 -> next smaller is 3
For 3 -> no smaller element on right => -1

"""

"""
Solution :

We use a Monotonic Increasing Stack and traverse the array from right to left.

Idea:
- We want the next smaller element, so we process elements from right side first.
- Maintain a stack which stores potential "next smaller candidates".

For each element nums[i]:

1. Remove all elements from stack which are greater than or equal to nums[i],
   because they cannot be the next smaller element for nums[i].

2. After popping:
   - If stack is empty → no smaller element exists on right → res[i] = -1
   - Else → stack[-1] is the next smaller element → res[i] = stack[-1]

3. Push nums[i] into the stack for future elements.

Each element is pushed and popped at most once → O(n) time.

TC -> O(n)
SC -> O(n)

"""

def next_smaller(nums):
    if not nums:
        return []

    stack = []
    res = [0] * len(nums)

    res[len(nums) - 1] = -1
    stack.append(nums[len(nums) - 1])

    for i in range(len(nums) - 2, -1, -1):
        while stack and stack[-1] >= nums[i]:
            stack.pop()

        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]

        stack.append(nums[i])

    return res