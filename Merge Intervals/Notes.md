Merge Intervals [start:end] :

- Where to apply :

1) Ranges

2) Intervals

- When to apply :

1) Overlap

2) Conflict

3) Merge

4) Free Time

5) Simultaneous Usage

6) Rooms / Load / CPU / Meeting

# 2 Steps to cover :

1) To know whether merging is required or not :

- Sort on basis of start
  if end 1 < start 2 -> Non-overlap
  if end 1 >= start 2 -> overlap

  [start 1 : end 1] , [start 2 : end 2] -
  start 1 < end 1 , start 2 < end 2 , start 1 < start 2

  Final Range -
  [start 1 : max(end 1, end 2)]

2) To actually merge the intervals :

- First sort all intervals on basis of start

- Assume first interval is current interval

  [start1 : end1]

- Now compare it with every next interval

  [start2 : end2]

- If overlap exists :

  end1 >= start2

  merge both intervals by updating

  end1 = max(end1,end2)

  -> we extend current interval to include next interval

- If overlap does not exist :

  end1 < start2

  current interval is completed

  store [start1:end1] in answer

  and make second interval the new current interval

  start1 = start2
  end1 = end2

  -> we start a new merged interval

- After loop ends,

  last active interval is still not stored,
  so add it separately into answer

# Intuition :

We always try to keep one "active merged interval"
and keep extending it as long as overlap exists

When overlap breaks → we freeze it and start new one

# Key Idea :

"Extend if overlap, otherwise close and restart"

# Time Complexity :

- Sorting -> O(n log n)

- Traversing all intervals -> O(n)

- Total -> O(n log n)

# Space Complexity :

- O(n) for output array