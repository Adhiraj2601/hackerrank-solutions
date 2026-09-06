# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/find-smallest-missing-positive-integer/problem?isFullScreen=true
# Problem     Find the Smallest Missing Positive Integer
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-06, 05:25 p.m.
# Technique   hash-set-lookup
# Time        O(n)
# Space       O(n)
# Insight     The algorithm identifies the smallest missing positive integer by checking consecutive integers starting from one against a hash set containing all elements of the input array.
# Interview   Before: "I could sort the array and scan for the first gap, which takes O(n log n) time." After: "By using a hash set to store elements, I can achieve O(n) time complexity, though it requires O(n) extra space to handle the lookup efficiently."
# Pitfalls    (1) The implementation uses O(n) space, which violates the O(1) extra space constraint specified in the problem description.  (2) Failing to handle the empty array case correctly would return an incorrect result, though this code explicitly returns 1 for an empty input.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    if len(orderNumbers)==0:
        return 1
    num_set = set(orderNumbers)
    smallest_missing = 1
    while smallest_missing in num_set:
        smallest_missing += 1
        
    return smallest_missing

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
