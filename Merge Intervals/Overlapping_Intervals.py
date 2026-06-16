"""
Qn.

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals and return an array of the
non-overlapping intervals that cover all the intervals in the input.

Example:

Input:
    [[1,3],[2,6],[8,10],[15,18]]

Output:
    [[1,6],[8,10],[15,18]]

Explanation:
    [1,3] and [2,6] overlap, so they are merged into [1,6].
"""

"""
Solution :

We first sort the intervals based on their starting point.

Why sorting?

If intervals are sorted by start time, then any overlap can only
occur with the current active interval and the next interval in order.
This allows us to process everything in a single pass.

We maintain:
- start1 : start of the current merged interval
- end1   : end of the current merged interval
- output : stores final merged intervals

Initially, we set start1 and end1 using the first interval.

Then we iterate through the remaining intervals one by one.

For each interval [start2, end2]:

Case 1: Overlapping interval

If:
    end1 >= start2

then the intervals overlap.

Example:
    [1,5] and [3,7]

Since 5 >= 3, they overlap.

We merge them by extending the current interval:
    end1 = max(end1, end2)

Case 2: Non-overlapping interval

If:
    end1 < start2

then the current merged interval is finished.

We store:
    [start1, end1]

into output and start a new interval:
    start1 = start2
    end1   = end2

After finishing the loop, one last interval remains unadded,
so we append it to output.

Finally, return output.

Time Complexity : O(n log n)
    - Sorting takes O(n log n)
    - Single pass traversal takes O(n)

Space Complexity : O(n)
    - Output array stores merged intervals
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        output = []

        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1, len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
            else:
                output.append([start1, end1])
                start1 = start2
                end1 = end2

        output.append([start1, end1])

        return output