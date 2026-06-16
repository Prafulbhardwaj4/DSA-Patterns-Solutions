Stack :

- Functions :

1) Push

2) Pop

3) Top

4) Size

5) Empty -> Boolean type

------------------------------------------------------------

- Where to apply :

1) Items - Array / String / Linked List nodes

------------------------------------------------------------

- When to apply :

1) Left to Right traversal problems

2) Most recent element dependency

3) Matching / Catching / Cleaning problems

4) Reverse / Backtracking type behavior

5) When we need to process "last seen valid state"

------------------------------------------------------------

- Types of Stack :

1) Simple Stack
   (push, pop, top)

2) Monotonic Stack
   (increasing or decreasing order maintained)

3) Greedy Stack
   (decision depends on condition + last element)

------------------------------------------------------------

# Steps to implement (Template) :

Example -> Stack -> [I1, I2, I3, I4]

1) Traverse Left → Right

2) For each element:
   - check condition with stack top
   - decide whether to pop or not

3) Push element if required

4) Store result if needed (based on problem)

------------------------------------------------------------

# Core Idea :

We use stack when we need to check or compare with the most recent valid element

------------------------------------------------------------

# Intuition Example :

Suppose we have: 1 2 4 6

Now a new element 7 comes:

We don’t compare 7 with all elements,
we only compare with the most recent relevant element in stack.

So instead of full search → we use top of stack

------------------------------------------------------------

Example (1047 style problem):

String = "abbaca"

- push 'a'
- push 'b'
- next 'b' → matches top → pop both b’s
- next 'a' → matches previous a → pop

So stack always keeps only valid leftover characters

------------------------------------------------------------

# Analogy :

Stack is LIFO → Last In, First Out

Like a bullet magazine:
- last inserted bullet is used first

We traverse left → right and decide:

1) pick element (push)
2) ignore element
3) remove last picked element (pop)

based on last seen element condition

------------------------------------------------------------

# Key Idea :

"Use stack when decision depends on most recent element"