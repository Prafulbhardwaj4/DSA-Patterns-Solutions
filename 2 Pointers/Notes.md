
2 Pointers :

When will we apply :

- When Question will be of Array or Linked List (Not if qn is of Tree/Graph/Stack/Queue)

- If the data is already sorted or it could help if the data would be sorted

- Merge/Remove/Rearrange type problems

- Detect Cycle or it would be better if it is cycle (Linked list)

- Pair / Triplets / Quadruple type problems

# Steps to implement :

1) Take two pointers

   Usually:
    i  - left pointer (start of array / list)
    j  - right pointer (end of array / list)

   or sometimes both from same starting point depending on problem

2) Move pointers based on condition

   It will have decisions like :
    i  - increase left pointer
    ii - decrease right pointer
    iii - move both pointers

   On every iteration at least one pointer must move

3) Process elements at pointers

   Depending on question:
    - compare values
    - merge values
    - calculate condition (sum / diff / match)

4) Stop condition:

   while left <= right (or problem specific condition)

# Intuition :

- Instead of checking all pairs (O(n^2)),
  we reduce search space by using both ends or two positions

- We avoid unnecessary comparisons by eliminating invalid ranges

- Works best when structure is sorted or can be made useful by sorting

# Key Idea :

"Shrink the search space using two ends / two positions"

# Time Complexity :

- O(n) → single pass (most optimized cases)

- O(n log n) → if sorting is required

# Space Complexity :

- O(1) → no extra space used (excluding sorting)