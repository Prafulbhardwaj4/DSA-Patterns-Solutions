Linked List Reversal:

100[1,Null] 200[2,300] 300[3,400] 400[4,/o]

curr = 100
prev = Null

nex = curr.next
curr.next = prev
prev = curr
curr = nex

Now curr is at 200, and prev is at 100

and same loop runs while curr is not Null

At each step:
- we first store next node (to not lose the remaining list)
- then reverse the link
- then move prev and curr forward

At the end, curr becomes Null and prev reaches last node
which becomes new head

return prev (helper standing at last)

# Intuition :

We are basically reversing the direction of pointers one by one
so that original head becomes tail and tail becomes head

We do NOT create new nodes, we only change links

# Key Idea :

"Break link forward, build link backward"

# Steps :

1) Take three pointers:

   curr = head
   prev = None
   nex  = None

2) Traverse until curr is not None:

   - Store next node
     nex = curr.next

   - Reverse current node link
     curr.next = prev

   - Move prev forward
     prev = curr

   - Move curr forward
     curr = nex

3) When loop ends:

   curr = None
   prev = new head of reversed list

4) Return prev

# Time Complexity :

O(n) → each node visited once

# Space Complexity :

O(1) → no extra space used (in-place reversal)