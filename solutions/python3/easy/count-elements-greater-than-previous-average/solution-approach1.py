# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem?isFullScreen=true
# Problem     Count Elements Greater Than Previous Average
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-06, 05:25 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    if len(responseTimes)==0:
        return 0
    else:
        avg = responseTimes[0]
        count=0
        n=2
        for i in range(1, len(responseTimes)):
            if responseTimes[i]>avg:
                count+=1
            avg = ((avg*(n-1))+ responseTimes[i])//n
            n+=1
        return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
