"""
Qn. Interval List Intersections

We are given two lists of disjoint, sorted intervals:
firstList and secondList.

We need to find the intersection between these two lists,
i.e., all intervals where both lists overlap.

Each list is sorted based on start time and contains
non-overlapping intervals within itself.
"""

"""
Solution :

We will use the Two Pointer approach.

Since both lists are sorted and non-overlapping internally,
we can traverse them simultaneously using two pointers:
i for firstList and j for secondList.

At every step, we compare the current intervals:
firstList[i] and secondList[j].

Idea behind intersection:

Two intervals intersect only if:
    max(start1, start2) <= min(end1, end2)

If this condition holds, the overlapping interval is:
    [max(start1, start2), min(end1, end2)]

Why this works:

We always take the maximum of start times because
the overlap cannot begin before both intervals start.

We take the minimum of end times because
the overlap ends when the first interval ends.

Pointer movement strategy:

After processing an interval pair, we move the pointer
that has the smaller ending value.

Reason:
The interval which ends earlier cannot contribute
to any further intersections, so we safely discard it.

We repeat this process until one list is fully traversed.

Finally, we return the list of all intersections stored in output.

Time Complexity : O(n + m)
Space Complexity : O(1) excluding output space
"""

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        output = []

        while i < len(firstList) and j < len(secondList):
            start1 = firstList[i][0]
            end1 = firstList[i][1]
            start2 = secondList[j][0]
            end2 = secondList[j][1]

            if start1 <= start2:
                if end1 >= start2:
                    s = max(start1,start2)
                    e = min(end1,end2)
                    output.append([s,e])
            else:
                if end2 >= start1:
                    s = max(start1,start2)
                    e = min(end1,end2)
                    output.append([s,e])
            
            if end1 <= end2:
                i += 1
            else:
                j += 1
            
        return output