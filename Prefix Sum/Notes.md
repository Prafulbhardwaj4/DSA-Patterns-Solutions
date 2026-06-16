Prefix Sum :

- Where to implement :

1) Array

2) Subarrays

- When to implement :

1) Sum of subarrays

2) Count of subarrays

3) Sum of left/right

4) Pivot / Equilibrium problems

5) Range sum queries (multiple queries on same array)

6) When we need fast cumulative computation

7) Array having negative numbers :

   - if sum == k or sum % k = 0 is asked → we use HASHMAPS (prefix + frequency)
   - if shortest window with sum >= k is asked → we use Deque / Sliding Window (only positive cases)
   - if range sum is asked multiple times → we use Prefix Array (precompute + O(1) query)

# Why Sliding Window does not work on Negatives :

- Because sliding window relies on monotonic behavior of sum

- If we need to decrease sum → we move left pointer
- If we need to increase sum → we move right pointer

- This works only when adding elements always increases sum (positive numbers)

- With negatives:
  adding/removing elements can both increase or decrease sum unpredictably
  so window logic breaks

# Equation to calculate Prefix and Suffix :

- Prefix Array :

  for i in range(1,n):
      Prefix[i] = Prefix[i-1] + a[i-1]

  return Prefix

- Suffix Array :

  for i in range(n-2,-1,-1):
      Suffix[i] = Suffix[i+1] + a[i+1]

  return Suffix

# Relation :

Left + Right + arr[i] = Total Sum of the array

# Steps to implement :

1) Initiate Prefix Data structure (Array, Variable, HashMap...)

2) Loop over given array

3) Update Prefix / Maintain running sum

4) Check Condition / Answer using prefix value

# Intuition :

Instead of recomputing sum again and again,
we store previous computations and reuse them

This converts O(n^2) → O(n)