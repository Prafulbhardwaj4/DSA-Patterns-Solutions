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

If intervals are sorted by start time, then for any interval,
we only need to compare it with the currently active merged interval.
This allows us to process the intervals in a single pass.

We maintain:

- start1 : Start of the current merged interval.
- end1   : End of the current merged interval.
- output : Stores all merged intervals.

Initially, start1 and end1 are set using the first interval.

For every next interval:

    [start2, end2]

Case 1 : Overlapping Interval

If:

    end1 >= start2

then the current interval overlaps with the merged interval.

Example:

    [1,5] and [3,7]

Since 5 >= 3, they overlap.

We extend the merged interval by updating:

    end1 = max(end1, end2)

Case 2 : Non-Overlapping Interval

If:

    end1 < start2

then the current merged interval is complete.

We store:

    [start1, end1]

into output.

Then start a new merged interval:

    start1 = start2
    end1   = end2

After processing all intervals,
the final merged interval is still not added to output,
so we append it once after the loop.

Finally, return output.

Time Complexity : O(n log n)
    - Sorting takes O(n log n)
    - Single traversal takes O(n)

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