"""
Qn. We are given a linked list, and we need to reverse it

"""

"""
Explanation -> 

1) We can reverse Linked List's nodes for n numbers of times, 

Mean we can do this :

Given : 10 -> 20 -> 30 -> 40 -> 50

Modified : 30 -> 20 -> 10 -> 40 -> 50
or, instaead of running loop while curr is not None, we can run, while curr is not (any node)

2) Required rotations -> right - left + 1

3) If left == right, means only 1 node is needed to be reversed, 
   in that case we will directly return head, as nothing will be reversed

"""

"""

Example : 10 -> 20 -> 30 -> 40 -> 50
positions : 2,4
times : right - left + 1 : 
4 - 2 + 1 = 3

if at 2nd position, we start rotating  
our linked list will look like

10 -> 20 -> None  
40 -> 30 -> 20 -> None
50 -> None

But we wanted : 10 -> 40 -> 30 -> 20 -> 50

so we need to point :
10 -> 40 
and 
20 -> 50

"""

"""
Solution :

We will first move to the `left` position.

While moving, we will store the node just before the `left` position in `before`.

Example :

10 -> 20 -> 30 -> 40 -> 50

left = 2

Then,

before = 10
t = 20

Now `t` is standing at the first node that needs to be reversed.

We will start normal Linked List reversal from `t`, but instead of running the loop until `curr == None`,
we will only run it for:

times = right - left + 1

because only those nodes need to be reversed.

After reversal,

prev -> points to the head of reversed part

curr -> points to the node just after the reversed part

and `t` still points to the original left node, which has now become the tail of the reversed part.

Example :

10 -> 20 -> 30 -> 40 -> 50

left = 2
right = 4

After reversing 3 nodes:

10 -> 20 -> None

40 -> 30 -> 20 -> None

50 -> None

Now we need to reconnect the Linked List.

First connect the tail of reversed part to the remaining list:

t.next = curr

20 -> 50

Then connect the first part of the list to the reversed part:

before.next = prev

10 -> 40

Final Linked List:

10 -> 40 -> 30 -> 20 -> 50

Special Case :

If left == 1, there is no node before the reversed part,
so `before` will be None.

In that case, `prev` becomes the new head of the Linked List,
so we directly return `prev`.

TC -> O(n)

SC -> O(1)


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        t = head
        pos = 1
        before = None

        if head is None:
            return None
        
        if left == right:
            return head
        
        while pos < left:
            before = t
            t = t.next
            pos += 1
        
        curr = t
        prev = None

        times = right - left + 1

        while(times):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times -= 1

        t.next = curr

        if before:
            before.next = prev
            return head
        
        # If left == 1, there will be no before so we will just return prev
        return prev