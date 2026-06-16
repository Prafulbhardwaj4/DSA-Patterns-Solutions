"""
Qn. Given a linked list we need to find whether it is a linked list or not

"""

"""
Solution :

Initiate 2 pointers with head pointer
while fast and fast.next are not null
increase slow pointer with 1, and fast with 2
if slow is equals to fast return True
and if we ever exit out from while loop return

"""
from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
    
        while fast and fast.next:
            slow =  slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False