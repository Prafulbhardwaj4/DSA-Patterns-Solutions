"""
Qn. Given a linked list we need to find the start of the head

"""

"""
Solution :

First we will find whether it is a cyle or not, once it is,
we will divede the cycle into 3 parts :
l1 = head to start of cycle
l2 = start of cycle to meeting point
l3(c-l2) = meeting point to start of cycle(going froward from MP)
[or we can say the rest of the cycle]

slow will move, l1 + l2
fast will move, l1 + n.C + l2 (n = number of times fast completes cycle, C = number of nodes)
2(slow) = fast
solving which, equation => l = c - l2 (Putting n = 1)

So technically, if we run,
slow from head to starting point,  it will take l1 steps(by 1 position)
fast from meeting to starting , it will take C-l2 which is = l1 only(by 1 position)

So the point where both pointers will meet will be the head
"""


from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while(slow!=fast):
                    slow = slow.next
                    fast = fast.next
                return slow