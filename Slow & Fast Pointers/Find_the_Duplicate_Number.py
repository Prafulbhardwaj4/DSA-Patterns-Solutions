"""
Qn.

Given an array nums containing n + 1 integers,
where each integer is in the range [1, n],

There is exactly one repeated number.

We need to find and return that duplicate number.

"""

"""
Solution :

This is a classic Slow and Fast Pointer (Floyd Cycle Detection) problem.

We treat the array as a linked list.

Idea :

Each index points to the value at that index.

So we form a virtual linked list where :

next position = nums[current]

Since there is a duplicate number,
a cycle is formed in this structure.

We need to find the entry point of the cycle,
which is the duplicate number.

Step 1 : Cycle Detection

We start both pointers from index 0.

slow moves one step at a time :
slow = nums[slow]

fast moves two steps at a time :
fast = nums[nums[fast]]

We keep moving until both meet.

If there is a cycle,
slow and fast will eventually meet inside it.

This confirms that a duplicate exists.

Step 2 : Find Cycle Start (Duplicate Number)

Once slow == fast,
we reset slow back to 0.

Now we move both pointers one step at a time :

slow = nums[slow]
fast = nums[fast]

The point where they meet again
is the entry point of the cycle.

That index/value is the duplicate number.

Why this works :

- First phase detects intersection inside cycle
- Second phase finds exact start of cycle
  using equal distance property

At the end,
we return the value where both pointers meet.

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while(True):
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                slow = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
        
                return slow