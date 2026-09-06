# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/merge-and-sort-intervals/problem?isFullScreen=true
# Problem     Merge and Sort Intervals
# Difficulty  Medium
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-06, 05:30 p.m.
# Technique   sorting-and-linear-scan
# Time        O(N log N)
# Space       O(N)
# Insight     The algorithm maintains a list of merged intervals by sorting the input by start time and greedily extending the last interval in the result list whenever an overlap is detected.
# Interview   Before: "I would use a nested loop to compare every interval against every other interval." After: "Sorting by start time allows a single linear pass to merge all overlapping intervals in O(N log N) time, which is optimal for this problem."
# Pitfalls    (1) Failing to handle the empty input case, which results in an index error when accessing intervals[0].  (2) Forgetting to sort the intervals by start time, which breaks the greedy merge logic.  (3) Using an incorrect overlap condition, such as strictly less than instead of less than or equal to, which fails to merge adjacent intervals.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    if len(intervals)==0:
        return []
    intervals.sort(key=lambda interval: interval[0])
    merged  = [intervals[0]]
    i=1
    while i<len(intervals):
        if intervals[i][0]<=merged[-1][1]:
            merged[-1][1]=max(intervals[i][1],merged[-1][1])
        else:
            merged.append(intervals[i])
        i+=1
    return merged

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
