"""
Qn. We are given a linked list, and we need to reverse it

"""

"""
Solution :

We will use three pointers:

curr -> points to current node
prev -> points to previous node
nex -> stores the next node temporarily

Initially,
curr = head
prev = Null

Now while curr is not Null:

First we will store the next node in nex,
because after reversing the link, we will lose access to the remaining list.

nex = curr.next

Then we will reverse the current node's pointer,

curr.next = prev

Now current node is pointing backwards.

After that, move prev one step ahead,

prev = curr

and move curr to the next node stored in nex,

curr = nex

This process continues until curr becomes Null.

At the end, prev will be standing at the last node of the original list,
which becomes the new head of the reversed linked list.

So we return prev.

TC -> O(n)
SC -> O(1)
"""

def reverse(head):
        curr = head 
        prev = None

        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        return prev