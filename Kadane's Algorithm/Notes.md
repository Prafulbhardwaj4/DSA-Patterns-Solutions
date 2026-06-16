Kadane's Algorithm (Array includes negative, positive, neutral) :

- When to use :

1) When a contiguous subarray is given, and we need to find its (best - min or max) :
    i   - sum
    ii  - product
    iii - frequency

2) When we are forced to take decisions on every element,
   and we want the best possible result ending at each index

3) When the answer depends on "continuous contribution" of elements
   (no skipping, no reordering)

4) When we need:
   - maximum subarray sum
   - minimum subarray sum
   - maximum gain / profit type problems
   - maximum difference in contiguous segment

# Steps to implement :

1) At every i, we need to find best ending at i

   It will have 2 options :
    i  - either add itself with previous data
         -> extend previous subarray
         -> current value contributes to ongoing result

    ii - or start with itself only
         -> discard previous contribution
         -> restart from current element

   So general form:
   bestEndingHere = max(bestEndingHere + arr[i], arr[i])

2) Maintain a global answer variable

   Because every index gives a possible best subarray ending there,
   but we need overall best among all of them

   So:
   res = max(res, bestEndingHere)

3) Initially:

   bestEndingHere = arr[0]
   res = arr[0]

4) At every step:

   we continuously update:
    - best subarray ending at i
    - global best answer so far

# Intuition :

- We never lose track of previous best
- But we are always ready to restart if current element is better alone
- This avoids carrying bad negative sums forward

# Key Idea :

"At every point, decide whether to extend or restart"

# Time Complexity :

- O(n) → single traversal

# Space Complexity :

- O(1) → only variables used