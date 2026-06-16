"""
Qn. Insert Interval

We are given a list of non-overlapping intervals sorted by start time,
and a new interval. We need to insert the new interval into the correct
position and merge overlapping intervals if necessary.
"""

"""
Solution :

We will use a two-step approach:
1. First, insert the new interval into its correct sorted position.
2. Then, merge all overlapping intervals in a single pass.

The idea is to maintain sorted order first, and then apply the standard
"merge intervals" logic.

Why this works:

Since the input intervals are already sorted by start time, we only need
to ensure that the new interval is placed in the correct position so that
the list remains sorted. Once sorted, merging becomes straightforward.

Step 1: Insertion Phase

We iterate through the intervals and compare each interval's start time
with the new interval's start time.

- If we have not yet inserted the new interval and the current interval
  starts after or at the new interval's start, we insert the new interval
  before it.
- Otherwise, we simply add the current interval.

At the end, if the new interval was never inserted (it belongs at the end),
we append it.

This produces a new sorted list called output1.

Step 2: Merge Phase

We now iterate through output1 and merge overlapping intervals.

We maintain:
- start1, end1 : the current interval being tracked
- output2 : final result list

For each interval:
- If current interval overlaps with previous (end1 >= start2),
  we merge them by updating end1 = max(end1, end2).
- Otherwise, we push the previous interval into output2 and
  reset start1, end1 to the current interval.

At the end, we append the last interval being tracked.

Finally, output2 contains all merged intervals after insertion.

Time Complexity : O(n)
Space Complexity : O(n)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output1 = []
        output2 = []
        inserted = False
        
        if not intervals:
            return [newInterval]
        for i in range(len(intervals)):
            if not inserted and intervals[i][0] >= newInterval[0]:
                output1.append(newInterval)
                inserted = True
            output1.append(intervals[i])
        if not inserted:
            output1.append(newInterval)
        
        start1 = output1[0][0]
        end1 = output1[0][1]
        
        for i in range(1, len(output1)):
            start2 = output1[i][0]
            end2 = output1[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
            else:
                output2.append([start1, end1])
                start1 = start2
                end1 = end2

        output2.append([start1, end1])

        return output2