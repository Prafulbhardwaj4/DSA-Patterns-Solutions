"""
Qn.

Given a singly linked list,

we need to find the middle node of the linked list.

If there are two middle nodes,
return the second middle node.

"""

"""
Solution :

This is a classic Slow and Fast Pointer problem.

We use two pointers:

slow -> moves one step at a time
fast -> moves two steps at a time

Idea :

- slow explores each node
- fast explores twice as fast

So when fast reaches the end,
slow will be exactly at the middle.

Steps :

1) Initialize both pointers at head

   slow = head
   fast = head

2) Move pointers until fast reaches end:

   while fast and fast.next:

       slow = slow.next
       fast = fast.next.next

3) When loop ends:

   fast has reached null (end of list)
   slow is at middle node

Why this works :

Because fast covers 2 nodes in one move,
while slow covers only 1 node.

So distance traveled ensures that
slow lands exactly halfway when fast finishes.

Edge Case :

If list has even number of nodes,
there are two middle nodes,
and this approach returns the second middle node,
as required.

Finally, return slow.

"""

from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow