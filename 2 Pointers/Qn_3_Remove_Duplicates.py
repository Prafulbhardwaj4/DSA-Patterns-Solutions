"""
Qn. We are given a sorted colony of houses where houses belonging to the same
category are placed together. We need to keep only one representative house
from each unique category at the front and return the number of unique categories.

"""
"""
Example:
A A B B B C C D D

"""
"""
Solution:

We appoint two people:

1. Officer:
   - Stands at the last approved unique category house.
   - Maintains the front section containing only unique categories.

2. CM:
   - Walks through the colony and inspects every house.

Initially, the first house is automatically approved, so:
Officer = first house
CM = second house
Unique count = 1

Now CM starts moving:

- If CM finds a house belonging to the same category as the previous house,
  it is a duplicate, so he simply moves ahead.

- If CM finds a new category,
  he informs the Officer.

- The Officer then allocates the next position in the approved section
  to this newly discovered category.

- The unique category count is increased by 1.

This process continues until CM reaches the end of the colony.

At the end:
- The front section contains exactly one house from each category.
- The count represents the total number of unique categories.

TC -> O(n)
SC -> O(1)

"""

class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            officer = 0
            res = 1
            cm = 1

            while cm < len(nums):
                if nums[cm] == nums[cm-1]:
                    cm += 1
                    continue
                nums[officer + 1] = nums[cm]
                officer += 1
                res += 1
                cm += 1
            return res