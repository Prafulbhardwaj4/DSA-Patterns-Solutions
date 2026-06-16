Slow and Fast Pointers :

- It can be implemented on :

1) Single variable / number transformation problems

2) Array

3) String

4) Linked List

# When we decide whether to use this or not (if we need to find if it is there or not) :

1) Cycle detection

2) Loop detection

3) Repeated behavior / repeating state

4) Starting point of cycle

5) Middle of linked list

6) Detect infinite repetition in function/state transitions

------------------------------------------------------------

# Steps to implement Slow and Fast Pointers :

1) Initiate 2 pointers:

   slow and fast

   Both start from same position:
   - head (Linked List)
   - index 0 (Array/String)
   - initial number (math problems)

------------------------------------------------------------

2) Shift pointers:

   slow moves 1 step
   fast moves 2 steps

   Examples:
   - Linked List:
       slow = slow.next
       fast = fast.next.next

   - Array:
       slow = slow + 1 step
       fast = fast + 2 steps

   - Number transformation:
       slow = f(slow)
       fast = f(f(fast))

------------------------------------------------------------

3) Core movement logic:

   while fast != null and fast.next != null:

       slow = slow.next
       fast = fast.next.next

       if slow == fast:
           cycle detected

------------------------------------------------------------

# Outcomes based on problem type :

- If need to detect cycle:

    return True when slow == fast

------------------------------------------------------------

- If need to find start of cycle:

    when slow == fast:
        move slow to head
        then move both slow and fast one step at a time

    where they meet again = cycle start

------------------------------------------------------------

- If need to find middle of linked list:

    slow starts at head
    fast starts at head

    move:
        slow = slow.next
        fast = fast.next.next

    when fast reaches null:
        slow is at middle

------------------------------------------------------------

# Important Notes :

- fast must always check fast != null AND fast.next != null
- otherwise null.next will give error

# Key Idea :

"Fast pointer reaches ahead quickly and helps detect cycles / middle efficiently"

# Time Complexity :

O(n)

# Space Complexity :

O(1)