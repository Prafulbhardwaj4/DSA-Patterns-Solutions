Sliding Window :

It either shrinks and expands using low and high pointers

# When we increase low, the window shrinks
# When we increase high, the window expands

When we will apply Sliding Windows :

1) Array or String (not on Linked List)

2) Sub-array or Sub-string → must be continuous

3) When we are trying to find :
   maximum, minimum, longest, shortest, sum, count, average,
   at most k, at least k, exactly k

# Sliding Window are of 2 types :

1) Fixed Size Window :

- Length of sub-array or sub-string is fixed

When k size is given:

low = 0
high = k - 1

Then we compute result for first window

After that:

- remove arr[low] from result
- low += 1
- high += 1
- add arr[high] to result

Repeat until high reaches end

# Idea :

We reuse previous window computation instead of recomputing again

------------------------------------------------------------

2) Dynamic / Variable Size Window :

- Window size is not fixed
- We adjust window based on condition

When k size is not given:

low = 0
high = 0

Run loop while high < n:

- include arr[high] into window info

- check condition

- if condition is violated:
    shrink window from left
    while condition is not valid:
        remove arr[low]
        low += 1

- then move high forward

# Idea :

Expand until invalid, then shrink until valid

------------------------------------------------------------

# Steps to apply :

1) Identify Pattern

2) Fixed / Variable Window

3) Define Window Data (sum / freq / count / etc.)

4) Update Window while moving pointers

------------------------------------------------------------

# For Maximum Window Problems :

1) We try to maintain a valid window

2) We expand window first

3) We shrink only when condition becomes invalid

4) Goal is to maximize window size / answer

------------------------------------------------------------

# For Minimum Window Problems :

1) We try to maintain a valid window

2) We expand until condition becomes valid

3) Once valid → we shrink to minimize window

4) Goal is to find smallest valid window

------------------------------------------------------------

# Key Difference :

- Maximum Window:
  shrink when condition becomes INVALID

- Minimum Window:
  shrink when condition becomes VALID