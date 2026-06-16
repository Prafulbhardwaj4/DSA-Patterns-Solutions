"""
Qn.

Given two arrays start and end representing the start and end times
of N meetings, find the minimum number of meeting rooms required so
that all meetings can be scheduled without any overlap.

A room can only host one meeting at a time.
"""

"""
Solution :

We will use the Two Pointer (Sweep Line) approach.

The idea is to separately sort the start times and end times.
This allows us to simulate the process of meetings starting and ending
in chronological order.

We maintain two pointers:
- i → tracks the next meeting start time
- j → tracks the earliest ending meeting

We also maintain:
- room → current number of active meetings (rooms in use)
- res → maximum number of rooms needed at any point

Why this works:

At any moment:
- If a meeting starts before the earliest ending meeting finishes,
  we need a new room.
- If a meeting starts after or at the time a meeting ends,
  we can reuse a room.

So we compare:
    start[i] and end[j]

Case 1: New meeting starts before earliest end
    start[i] < end[j]
→ A new meeting overlaps
→ Increase room count
→ Move to next start time (i += 1)

Case 2: A meeting has ended before next starts
    start[i] >= end[j]
→ A room becomes free
→ Decrease room count
→ Move end pointer (j += 1)

At every step, we update:
    res = max(res, room)

Finally, res contains the maximum number of rooms used
at any time, which is the minimum rooms required.

Time Complexity : O(n log n)
    - Sorting start and end arrays

Space Complexity : O(1)
    - No extra space apart from variables
"""

class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        start.sort()
        end.sort()
        i = j = room = res = 0
        
        while i < len(start):
            if start[i] < end[j]:
                room += 1
                i += 1
            else:
                room -= 1
                j += 1
                
            res = max(res,room)
        
        return res
        
