"""
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
"""

def sum_of_intervals(intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    # Initialize the result with the first interval
    result = intervals[0][1] - intervals[0][0]
    
    # Initialize a set for processed intervals (duplicates)
    processed_intervals = {intervals[0]}
    
    # Iterate through the intervals and update the result
    for i in range(1, len(intervals)):
        # Check if the current interval overlaps with the previous interval
        if intervals[i][0] < intervals[i-1][1]:
            # Check if the current interval has been processed before
            if intervals[i] in processed_intervals:
                continue
            # Calculate the overlap length
            overlap = min(intervals[i][1], intervals[i-1][1]) - max(intervals[i][0], intervals[i-1][0])
            # Update the result with the overlap length
            result += overlap
        else:
            # If the intervals do not overlap, update the result with the current interval
            result += intervals[i][1] - intervals[i][0]
            processed_intervals.add(intervals[i])
    
    return result
